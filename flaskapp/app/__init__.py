from flask import Flask, render_template
from os import environ

env = dict(environ)

def create_app(testing=False):
	app = Flask(__name__)
	@app.route('/')
	def test():
		return render_template('index.html')
	return app
