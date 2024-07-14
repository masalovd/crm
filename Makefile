.PHONY: run-server makemigrations migrate collectstatic \
		superuser install update


update: install migrate;

run-server:
	poetry run python -m crm.manage runserver

makemigrations:
	poetry run python -m crm.manage makemigrations

migrate:
	poetry run python -m crm.manage migrate

collectstatic:
	poetry run python -m crm.manage collectstatic --no-input

superuser:
	poetry run python -m crm.manage createsuperuser

install:
	poetry install