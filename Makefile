#!/bin/bash

create-virtualenv-install-requirements:
	virtualenv venv -p python3 --no-site-packages; \
	. venv/bin/activate; \
	venv/bin/pip install -r requirements.txt; \

activate-virtualenv-run-app:
	. venv/bin/activate; \
	venv/bin/python paniyosite/manage.py runserver; \

shell:
	. venv/bin/activate; \
	venv/bin/python paniyosite/manage.py shell; \

migrations:
	. venv/bin/activate; \
	venv/bin/python paniyosite/manage.py makemigrations; \

migrate:
	. venv/bin/activate; \
	venv/bin/python paniyosite/manage.py migrate; \

superuser:
	. venv/bin/activate; \
	venv/bin/python paniyosite/manage.py createsuperuser; \

install: create-virtualenv-install-requirements

run: activate-virtualenv-run-app