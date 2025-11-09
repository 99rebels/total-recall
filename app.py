
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
  entire_table = (
    supabase.table("first-table")
    .select("*")
    .execute()
)
  html_build = "<html><body>"
  html_end_string = "</body></html>"
  html_build = html_build + "<ul>"

  for rows in entire_table.data:
    for data in rows.values():
      html_build = html_build + "<li>" + str(data) + "</li>"
  html_build = html_build + "</ul>"

  return html_build + html_end_string

@app.route("/form_input")
def form_input():
  return render_template("form_input.html")

@app.route("/form_output", methods =["Get"])
def form_output():
  username = request.args.get("username")
  password = request.args.get("password")
  return str(username) + " " + str(password)


if __name__ == "__main__":
  app.run(debug = True)
  