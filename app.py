
from dotenv import load_dotenv
load_dotenv()

from datetime import datetime, timedelta
from utils.db_client import get_notes
from flask import Flask, request, render_template, url_for, redirect
import os
import json


from supabase import create_client #Supabase Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)




import google.generativeai as genai #Google Gemini Client

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")





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
  .execute()
  )

  return redirect(url_for("submitted_notes"))

@app.route("/submitted_notes")
def submitted_notes():
  return render_template("submitted_notes.html")


# A function to work out the dates I'll be using to retrieve relavent notes from the database for that day and sends it to todays_notes.html to be iterated through and displayed with jinja.
@app.route("/todays_notes", methods = ["GET", "POST"])

def todays_notes():

  question_request = request.args.get("generate_questions")
  todays_notes = ""

  if question_request:
    
    user_questions = request.args.get("user_questions")
    note_id = request.args.get("note_id")  
    llm_questions = generate_questions(note_id, user_questions)

    todays_notes = all_notes(note_id, llm_questions)
  else:
    todays_notes =  all_notes()

  print(todays_notes)
  return render_template("todays_notes.html", todays_notes=todays_notes)



def generate_questions(note_id, user_questions):
 
  note = (
    supabase.table("notes")
    .select("*")
    .eq("id", note_id)
    .execute()
  )

  note = note.data[0]
  
  prompt = f"""Context: this is a tool created to test a users knowlege on the provided content. They have created questions for themselves, but your job is to create some additonal ones to test them on the content further.
  JOB: from the notes, subject and topic, create ONLY FIVE additonal questions (make sure theyre not duplicates of the ones given by the user). Only create questions where answers are pretty confindentally present in the notes provided to you. You are allowed to experiment somewhat in creating the questions, but answers must be at least hinted to in the notes. The relavent info will be provided to you now: user notes: {note["notes"]}, subject: {note["subject"]}, topic: {note["topic"]}, user questions: {user_questions}. return ONLY valid Json in this format: ["question 1", "question 2", "question 3", ...]. Do NOT include code fences, explanations, backticks, or markdown."""

  

  response = model.generate_content(prompt) 


  llm_questions = json.loads(response.text)

  return llm_questions

  
def all_notes(note_id = None, llm_questions = None):
  
  date = datetime.now()
  day_prior = str(date - timedelta(days=1))
  week_prior = str(date - timedelta(days=7))
  month_prior = str(date - timedelta(days=30))
  three_month_prior = str(date - timedelta(days=90))


  day_prior_notes = get_notes(day_prior, note_id, llm_questions)
  week_prior_notes = get_notes(week_prior, note_id, llm_questions)
  month_prior_notes = get_notes(month_prior, note_id, llm_questions)
  three_month_prior_notes = get_notes (three_month_prior, note_id, llm_questions)

  
  note_list ={}

  note_list.update({"Yesterday": day_prior_notes, "Last Week": week_prior_notes, "Last Month": month_prior_notes, "Three Months Ago": three_month_prior_notes})

  return note_list



if __name__ == "__main__":
  app.run(debug = True)
  