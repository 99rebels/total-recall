from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template ("index.html")

@app.route("/notes")
def notes():
  return render_template ("notes.html")

@app.route("/notes/<date>")
def notes_today(date):
  return "<html><body><h4>You're notes for " + str(date) + " are available </h4></body></html>"

if __name__ == "__main__":
  app.run(debug = True)
  