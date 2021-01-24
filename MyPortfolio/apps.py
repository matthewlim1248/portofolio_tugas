from flask import Flask, render_template

from datetime import datetime

app = Flask(__name__)

@app.route("/") #default route => default page
def index():
	return "<h3>Hello Flask ...</h3>"

@app.route("/MyPortfolio")
def portfolio():
	page = render_template("htmls.html")
	return page