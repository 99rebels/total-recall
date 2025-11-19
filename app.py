
from dotenv import load_dotenv
from datetime import datetime, timedelta
load_dotenv()
from utils.db_client import get_notes

import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/") 
def index():
  return render_template("index.html")


# function to get all subjects from the database (without duplication) to display to the user as a dropdown menue of options
@app.route("/subject_input")
def form_input():

  subject_options = (
    supabase.table("notes")
    .select("subject")
    .execute()
  )

  subject_collection = []

  for subject in subject_options.data:
    for subject in subject.values():
      if subject in subject_collection:
        continue
      else:
        subject_collection.append(subject)

  return render_template("subject_choice.html", subject_collection = subject_collection)



# function that takes the subject the user has chosen as an argument to get all the topics in the DB equal to the subject and then displays these topics as a dropdown menu of options.
@app.route("/notes_form", methods =["GET"]) 
def get_topic():
  subject = request.args.get("subject")
  topics = (
    supabase.table("notes")
    .select("topic")
    .eq("subject", str(subject))
    .execute()
  )
  topic_collection = []
  for topics in topics.data:
    for topic in topics.values():
      if topic in topic_collection:
        continue
      else:
        topic_collection.append(topic)
  return render_template("notes_form.html", topic_collection = topic_collection, subject = subject, topic=topic)


# Function that inserts new data depending on the subject, topic, notes and questions a user added.
@app.route("/form_submit", methods=["GET", "POST"]) 
def notes():
  subject = request.args.get("subject")
  notes = request.args.get("notes")
  questions = request.args.getlist("question")
  topic = request.args.get("topic")
  date = request.args.get("date")

  print(questions)
  send_notes = (
    supabase.table("notes")
    .insert({"created_at":date, "subject":subject, "topic": topic, "notes": notes,}) 
    .execute()
  )
  
  main_id =  send_notes.data[0]["id"]

  rows = ([{"main_id":main_id, "question":question, "created_at":date } for question in questions])
  print(rows)

  (supabase.table("questions")
  .insert(rows) 
  .execute())

  return redirect(url_for("submitted_notes"))

@app.route("/submitted_notes")
def submitted_notes():
  return render_template("submitted_notes.html")


# A function to work out the dates I'll be using to retrieve relavent notes from the database for that day and sends it to todays_notes.html to be iterated through and displayed with jinja.
@app.route("/todays_notes")
def todays_notes():
  date = datetime.now()
  day_prior = str(date - timedelta(days=1))
  week_prior = str(date - timedelta(days=7))
  month_prior = str(date - timedelta(days=30))
  three_month_prior = str(date - timedelta(days=90))


  day_prior_notes = get_notes(day_prior)
  week_prior_notes = get_notes(week_prior)
  month_prior_notes = get_notes(month_prior)
  three_month_prior_notes = get_notes (three_month_prior)
  
  return render_template("todays_notes.html", day_prior_notes = day_prior_notes, week_prior_notes = week_prior_notes, month_prior_notes = month_prior_notes, three_month_prior_notes = three_month_prior_notes, date=date)


if __name__ == "__main__":
  app.run(debug = True)
  