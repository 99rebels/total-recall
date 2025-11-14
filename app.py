
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

@app.route("/subject_input")
def form_input():

  subject_options = (
    supabase.table("main-table")
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




@app.route("/subject_output", methods =["GET"])
def subject_output():
  subject = request.args.get("subject")
  topics = (
    supabase.table("main-table")
    .select("topic")
    .eq("subject", str(subject))
    .execute()
  )
  topic_collection = []
  for topics in topics.data:
    for topic in topics.values():
      topic_collection.append(topic)
  return render_template("notes_form.html", topic_collection = topic_collection, subject = subject, topic=topic)



@app.route("/notes_form", methods=["GET", "POST"])
def notes():
  subject = request.args.get("subject")
  notes = request.args.get("notes")
  questions = request.args.get("questions")
  topic = request.args.get("topic")
  date = request.args.get("date")

  (
    supabase.table("main-table")
    .insert({"created_at":date, "subject":subject, "topic": topic, "subject": subject, "notes": notes, "questions": questions})
    .execute()
  )
  return redirect(url_for("submitted_notes"))

@app.route("/submitted_notes")
def submitted_notes():
  return render_template("submitted_notes.html")

def date_checker(): # A function to work out the dates I'll be using to retrieve relavent notes from the database #
  date = datetime.now()
  day_prior = str(date - timedelta(day=1))
  week_prior = str(date - timedelta(day=7))
  month_prior = str(date - timedelta(day=30))
  three_month_prior = str(date - timedelta(day=90))
  return todays_notes(day_prior, week_prior, month_prior, three_month_prior)

@app.route("/todays_notes")
def todays_notes():
  date = datetime.now()
  day_prior = str(date - timedelta(days=1))
  week_prior = str(date - timedelta(days=7))
  month_prior = str(date - timedelta(days=30))
  three_month_prior = str(date - timedelta(days=90))


  day_prior_data = get_notes(day_prior)
  week_prior_data = get_notes(week_prior)
  month_prior_data = get_notes(month_prior)
  three_month_prior_data = get_notes(three_month_prior)

  return render_template("todays_notes.html", day_prior_data = day_prior_data, week_prior_data = week_prior_data, month_prior_data = month_prior_data, three_month_prior_data = three_month_prior_data, date=date)


if __name__ == "__main__":
  app.run(debug = True)
  