from flask import g, current_app
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from .models import Base
from functools import wraps

db = None

def init_db(app):
	global db
	db = create_engine(app.config['DATABASE_URI'])
	insp = inspect(db)
	if not insp.has_table("menu_item"):
		print("Creating database tables...")
		Base.metadata.create_all(db)
	print("Database initialized.")

def uses_database(func):
	@wraps(func)
	def deco(*args, **kwargs):
		g.db = Session(db)
		g.db.begin()
		return func(*args, **kwargs)
	return deco




