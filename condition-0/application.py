from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def index():
	date = datetime.datetime.now()
	new_year = date.month == 1 and date.month == 1
	new_year=True
	return render_template("index.html", new_year=new_year)