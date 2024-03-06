#!/bin/bash
. venv/bin/activate
pip install -e .
export POSTGRES_USER=_
export POSTGRES_PASSWORD=_
export POSTGRES_HOST=_
export POSTGRES_PORT=_
export POSTGRES_DB=_
if [ "$#" -eq 1 -a "$1" = "test" ]
	then coverage run -m pytest && coverage report
fi
flask --app "sushiapp:create_app(config='TestingConfig')" run
