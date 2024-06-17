from flask import Flask, session, g
from .config import env
from .home import bp as bp_home
from .menu import bp as bp_menu
from .api import bp as bp_api
from .db import init_db
from .admin import bp as bp_admin

bps = [
	bp_home,
	bp_menu,
	bp_api,
	bp_admin
]

#	This function generates and configures the app
#	The arguments are important for running unit tests
def create_app(config='DevelopmentConfig', dbOverride=None):
	app = Flask(__name__)
	app.config.from_object('sushiapp.config.' + config)
	if dbOverride:
		app.config['DATABASE_URI'] = dbOverride
	for bp in bps:
		app.register_blueprint(bp)
#	Initiate database and ensure database sessions are committed after a
#	request is handled
	init_db(app)
	@app.teardown_appcontext
	def teardown(exception=None):
		if 'db' in g:
			if exception is None:
				g.db.commit()
			g.db = None
	return app