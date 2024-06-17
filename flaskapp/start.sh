#!/bin/bash
rm test.db
. venv/bin/activate
pip install -e .
export POSTGRES_USER=_
export POSTGRES_PASSWORD=_
export POSTGRES_HOST=_
export POSTGRES_PORT=_
export POSTGRES_DB=_
export SECRET_KEY=testkey
export FLASK_DEBUG=true
if [ "$#" -eq 1 -a "$1" = "test" ]
	then coverage run -m pytest && coverage report && coverage html
fi
flask --app "sushiapp:create_app(config='TestingConfig')" run
