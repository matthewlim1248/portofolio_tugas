
from flask import Flask, render_template, request

from models import *
from config import config
thisConfig = Config()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABSE_URI"] = thisConfig.DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False