.PHONY: run-server run-pre-commit makemigrations migrate collectstatic \
		superuser install install-pre-commit update


update: install migrate install-pre-commit;

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

run-pre-commit:
	poetry run pre-commit run --all-files

install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

install:
	poetry install
