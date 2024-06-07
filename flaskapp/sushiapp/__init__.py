from flask import Flask, session, g
from .config import env
from .home import bp as bp_home
from .menu import bp as bp_menu
from .api import bp as bp_api
from .db import init_db

bps = [
	bp_home,
	bp_menu,
	bp_api
]

def create_app(config='DevelopmentConfig'):
	app = Flask(__name__)
	app.config.from_object('sushiapp.config.' + config)
	for bp in bps:
		app.register_blueprint(bp)
	init_db(app)
	@app.teardown_appcontext
	def teardown(exception=None):
		if 'db' in g:
			if exception is None:
				g.db.commit()
			g.db = None
	return app