
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
  return""

@app.route("/subject_input")
def form_input():

  subject_options = (
    supabase.table("main-table")
    .select("subject")
    .execute()
  )

  html_build = "<html><body><form action = \"/subject_output\" name=\"subject\"><select name=\"subject\">"
  submit = "<input type=\"submit\" id=\"submit\">"
  html_end = "</form></body></html>"
  subject_collection = []

  for subject in subject_options.data:
    for subject in subject.values():
      if subject in subject_collection:
        continue
      else:
        subject_collection.append(subject)

  for subject in subject_collection:
    html_build = html_build + "<option>" + str(subject) + "</option>"
  html_build = html_build + "</select>"

  return html_build+submit+html_end




@app.route("/subject_output", methods =["GET"])
def subject_output():
  subject = request.args.get("subject")
  topics = (
    supabase.table("main-table")
    .select("topic")
    .eq("subject", str(subject))
    .execute()
  )
  
  html="<html><body><form action = \"/notes\"><select>"
  for topics in topics.data:
    for topic in topics.values():
      html += "<option>" + topic + "</option>"
  html+="</select><input type = \"text\" name =\"notes\" placeholder = \"notes\"><input type = \"text\" name =\"questions\" placeholder = \"questions\"> <input type = \"submit\"></form></body></html>"
  return html


@app.route("/notes")
def notes():
  notes = request.args.get("notes")
  questions = request.args.get("questions")

  html = "<html><body><h2> Your notes for today! </h2><h3> Notes: </h3>" + notes + "<h3> Questions: </h3>" + questions + "</body</html>"

  return html


if __name__ == "__main__":
  app.run(debug = True)
  