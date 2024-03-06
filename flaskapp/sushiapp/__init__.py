from flask import Flask, render_template
from .config import env

def create_app(config='DevelopmentConfig'):
	app = Flask(__name__)
	app.config.from_object('sushiapp.config.' + config)
	@app.route('/')
	def test():
		return render_template('index.html')
	return app
