BLACK ?= \033[0;30m
RED ?= \033[0;31m
GREEN ?= \033[0;32m
YELLOW ?= \033[0;33m
BLUE ?= \033[0;34m
PURPLE ?= \033[0;35m
CYAN ?= \033[0;36m
GRAY ?= \033[0;37m
WHITE ?= \033[1;37m
COFF ?= \033[0m

.PHONY: all shell build docker help load_initial_data migrate superuser test-django runserver makemigrations lint lint-fix

all: help

help:
	@echo -e "\n$(WHITE)Available commands:$(COFF)"
	@echo -e "$(CYAN)make runserver$(COFF)        - Runs the django app in the production container, available at http://127.0.0.1:8000"
	@echo -e "$(CYAN)make runserver-dev$(COFF)    - Runs the django app in the development container, available at http://127.0.0.1:8000"
	@echo -e "$(CYAN)make migrate$(COFF)          - Runs django's migrate command in the production container"
	@echo -e "$(CYAN)make migrate-dev$(COFF)      - Runs django's migrate command in the development container"
	@echo -e "$(CYAN)make makemigrations$(COFF)   - Runs django's makemigrations command in the production container"
	@echo -e "$(CYAN)make makemigrations-dev$(COFF)   - Runs django's makemigrations command in the development container"
	@echo -e "$(CYAN)make superuser$(COFF)        - Runs django's createsuperuser command in the production container"
	@echo -e "$(CYAN)make superuser-dev$(COFF)    - Runs django's createsuperuser command in the development container"
	@echo -e "$(CYAN)make shell$(COFF)            - Starts a Linux shell (bash) in the web production container"
	@echo -e "$(CYAN)make shell-dev$(COFF)        - Starts a Linux shell (bash) in the web development container"
	@echo -e "$(CYAN)make test$(COFF)             - Runs automatic tests on your python code"
	@echo -e "$(CYAN)make coverage$(COFF)         - Runs code test coverage calculation"


shell:
	@echo -e "$(CYAN)Starting Bash in the web production container:$(COFF)"
	@docker-compose -f docker-compose-prod.yml run --rm web python ./manage.py shell

shell-dev:
	@echo -e "$(CYAN)Starting Bash in the web development container:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py shell

build:
	@echo -e "$(CYAN)Creating Docker images for production:$(COFF)"
	@docker-compose -f docker-compose-prod.yml build

build-dev:
	@echo -e "$(CYAN)Creating Docker images for development:$(COFF)"
	@docker-compose -f docker-compose-dev.yml build

runserver:
	@echo -e "$(CYAN)Starting Docker container with the app in production.$(COFF)"
	@docker-compose -f docker-compose-prod.yml up -d
	@echo -e "$(CYAN)App ready and listening at http://127.0.0.1:8000.$(COFF)"

runserver-dev:
	@echo -e "$(CYAN)Starting Docker container with the app in development.$(COFF)"
	@docker-compose -f docker-compose-dev.yml up -d
	@echo -e "$(CYAN)App ready and listening at http://127.0.0.1:8000.$(COFF)"

test-django:
	@echo -e "$(CYAN)Running automatic django tests:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web py.test

coverage-django:
	@echo -e "$(CYAN)Running automatic code coverage check for Python:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web sh -c "coverage run -m py.test && coverage html && coverage report"

makemigrations:
	@echo -e "$(CYAN)Running django makemigrations for production:$(COFF)"
	@docker-compose -f docker-compose-prod.yml run --rm web python ./manage.py makemigrations $(cmd)

makemigrations-dev:
	@echo -e "$(CYAN)Running django makemigrations for development:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py makemigrations $(cmd)

migrate:
	@echo -e "$(CYAN)Running django migrations:$(COFF)"
	@docker-compose -f docker-compose-prod.yml run --rm web python ./manage.py migrate $(cmd)

migrate-dev:
	@echo -e "$(CYAN)Running django migrations:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py migrate $(cmd)

load_initial_data:
	@echo -e "$(CYAN)Loading django fixture:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py loaddata website/fixtures/initial.json

loadmanyprojects:
	@echo -e "$(CYAN)Loading lots of projects:$(COFF)"
	@docker-compose run --rm web python ./manage.py loadmanyprojects $(cmd)

superuser-dev:
	@echo -e "$(CYAN)Creating Docker images:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py createsuperuser $(cmd)

lint:
	@echo -e "$(CYAN)Running Black check:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web black --check .

lint-fix:
	@echo -e "$(CYAN)Running Black formatting:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web black .

shutdown:
	@echo -e "$(CYAN)Stopping services:$(COFF)"
	@docker-compose -f docker-compose.yml down

shutdown-dev:
	@echo -e "$(CYAN)Stopping services:$(COFF)"
	@docker-compose -f docker-compose-dev.yml down


logs:
	@echo -e "$(CYAN)Checking logs:$(COFF)"
	@docker-compose -f docker-compose-prod.yml logs -f

logs-dev:
	@echo -e "$(CYAN)Checking logs:$(COFF)"
	@docker-compose -f docker-compose-dev.yml logs -f
