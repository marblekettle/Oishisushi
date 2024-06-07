from os import environ

env = dict(environ)

class Config(object):
	TESTING = False
	SECRET_KEY = env['SECRET_KEY']

class TestingConfig(Config):
	TESTING = True
	DATABASE_URI = 'sqlite:///test.db'

class DevelopmentConfig(Config):
	DATABASE_URI = 'postgresql+psycopg://{}:{}@{}:{}/{}'.format(
		env['POSTGRES_USER'],
		env['POSTGRES_PASSWORD'],
		env['POSTGRES_HOST'],
		env['POSTGRES_PORT'],
		env['POSTGRES_DB']
	)
