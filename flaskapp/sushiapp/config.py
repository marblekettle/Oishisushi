from os import environ

env = dict(environ)

class Config(object):
	TESTING = False
	SECRET_KEY = env['SECRET_KEY']

#	The testing config is for running the app locally in a virtual environment
#	and creates a local Sqlite test database
class TestingConfig(Config):
	TESTING = True
	DATABASE_URI = 'sqlite://'

#	The development config is for running in a container, and is set up to
#	connect to a Postgresql database in a container defined by environment
#	variables defined in docker_compose.yml and the .env file
class DevelopmentConfig(Config):
	DATABASE_URI = 'postgresql+psycopg://{}:{}@{}:{}/{}'.format(
		env['POSTGRES_USER'],
		env['POSTGRES_PASSWORD'],
		env['POSTGRES_HOST'],
		env['POSTGRES_PORT'],
		env['POSTGRES_DB']
	)
