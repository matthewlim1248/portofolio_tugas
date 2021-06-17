
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):

	__tablename__= "users"
	id = db.Column(db.Integer, nullable=False)
	username = db.Column(db.String, primary_key=True, nullable= False, unique=True)
	password = db.Column(db.String, nullable=False)
	first_name = db.Column(db.String, nullable=False)
	last_name = db.Column(db.String, nullable=False)
	active = db.Column(db.Boolean, nullable=False, default=True)
	added_on = db.Column(db.DateTime, default=datetime.utcnow)
	last_active = db.Column(db.DateTime, default=datetime.utcnow)
	notes = db.relationship("Note", backref="note", lazy=True)

class Note(db.Model):

	__tablename__= "notes"
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	created_by = db.Column(db.String, db.ForeignKey("users.username"), nullable=False)
	title = db.Column(db.String, nullable=False, default="-")
	note = db.Column(db.String, nullable=True)
	created_on = db.Column(db.DateTime, default=datetime.utcnow)
	last_update = db.Column(db.DateTime, default=datetime.utcnow)
