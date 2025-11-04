from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
  greeting = "hello world again"
  return_html = "<html><body>" + greeting + "</body></html>"
  return return_html

if __name__ == "__main__":
  app.run(debug = True)