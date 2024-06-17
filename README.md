# Oishisushi
An app for my favorite food

## Requirements

Requires Python 3.x and Docker to be installed.
Supply a .env file with two lines for setting `POSTGRES_PASSWORD` and `SECRET_KEY`. Example:
```
POSTGRES_PASSWORD=a_good_p4ssword
SECRET_KEY=veryverysecret123
```

## How to run

Run `docker compose up --build` to deploy development mode
Or run `sh start.sh` in the `flaskapp` directory to run testing mode in a virtual environment.
Coverage tests can be run with `sh start.sh test`

If deployed with Docker, the webapp can be found at `http://localhost:8080` by default. If running in a virtual environment, the default is `http://localhost:5000`
