import pytest
import os
from sushiapp import create_app

@pytest.fixture()
def app():
	if os.path.exists('test.db'):
		os.remove('test.db')
	return create_app("TestingConfig")

@pytest.fixture()
def client(app):
	return app.test_client()
