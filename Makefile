run:
	python3 manage.py runserver

install:
	cp example.env .env
	python3 -m pip install --upgrade pip
	python3 -m venv venv
	source ./venv/bin/activate
	pip install -r requirements.txt

clndb:
	rm -rf ./apps/authnapp/migrations/00*
	rm -rf ./apps/directory/migrations/00*
	rm -rf ./apps/invoice/migrations/00*
	rm -rf ./apps/mainapp/migrations/00*
	rm -rf ./apps/personalacc/migrations/00*

	rm -rf ./data/postgresql/*

filldb:
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py dbimport

refac:
	isort .
	black -l120 .

