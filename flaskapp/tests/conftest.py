import pytest
import os
from sushiapp import create_app

@pytest.fixture()
def app():
	return create_app("TestingConfig")

@pytest.fixture()
def dbapp():
	if os.path.exists('test.db'):
		os.remove('test.db')
	return create_app("TestingConfig", dbOverride='sqlite:///test.db')

@pytest.fixture()
def client(app):
	return app.test_client()

@pytest.fixture()
def dbclient(dbapp):
	return dbapp.test_client()