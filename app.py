
from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

from flask import Flask, request, render_template

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
  return render_template("note_input.html", topic_collection = topic_collection, subject = subject, topic=topic)


@app.route("/notes", methods=["GET"])
def notes():
  subject = request.args.get("subject")
  notes = request.args.get("notes")
  questions = request.args.get("questions")
  topic = request.args.get("topic")

  (
    supabase.table("main-table")
    .insert({"subject":subject, "topic": topic, "subject": subject, "notes": notes, "questions": questions})
    .execute()
  )
  return render_template("todays_notes.html", notes=notes, questions=questions)


if __name__ == "__main__":
  app.run(debug = True)
  