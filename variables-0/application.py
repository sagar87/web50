from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello/<string:name>")
def index(name):
	return render_template("index.html", headline=name)

@app.route("/bye")
def bye():
	return render_template("index.html", headline="byebye")	