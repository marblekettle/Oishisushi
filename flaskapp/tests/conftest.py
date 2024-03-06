import pytest
from sushiapp import create_app

@pytest.fixture()
def app():
	return create_app("TestingConfig")

@pytest.fixture()
def client(app):
	return app.test_client()
