from flask import Flask, render_template, request, session
from flask_sessions import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


notes = []


@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		note = request.form.get("note")
		notes.append(note)

	return render_template("index.html", notes=notes)

@app.route("/more")
def more():
	return render_template("more.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
	if request.method == "GET":
		return "Please submit the form instead"
	else:
		name = request.form.get("name")
		return render_template("hello.html", name=name)