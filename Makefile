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

.PHONY: all help shell shell-dev build build-dev runserver runserver-dev collectstatic collectstatic-dev makemigrations makemigrations-dev migrate migrate-dev load-initial-data load-many-posts superuser superuser-dev shutdown shutdown-dev shutdown-volumes shutdown-volumes-dev logs logs-dev logs-interactive logs-interactive-dev coverage-django lint lint-fix test-project test-website test-users docker

all: help

help:
	@echo -e "\n$(WHITE)Available commands:$(COFF)"
	@echo -e "$(CYAN)make shell$(COFF)            - Starts a Linux shell (bash) in the web production container"
	@echo -e "$(CYAN)make shell-dev$(COFF)        - Starts a Linux shell (bash) in the web development container"
	@echo -e "$(CYAN)make build$(COFF)            - Builds production images"
	@echo -e "$(CYAN)make build-dev$(COFF)        - Builds development images"
	@echo -e "$(CYAN)make runserver$(COFF)        - Runs the django production app, available at http://127.0.0.1:8000"
	@echo -e "$(CYAN)make runserver-dev$(COFF)    - Runs the django development app, available at http://127.0.0.1:8000"
	@echo -e "$(CYAN)make collectstatic$(COFF)    - Runs the Django's collectstatic command"
	@echo -e "$(CYAN)make collectstatic-dev$(COFF)  - Runs the Django's collectstatic command in development"
	@echo -e "$(CYAN)make makemigrations$(COFF)   - Runs django's makemigrations command in the production container"
	@echo -e "$(CYAN)make makemigrations-dev$(COFF) - Runs django's makemigrations command in the development container"
	@echo -e "$(CYAN)make migrate$(COFF)          - Runs django's migrate command in the production container"
	@echo -e "$(CYAN)make migrate-dev$(COFF)      - Runs django's migrate command in the development container"
	@echo -e "$(CYAN)make load-initial-data$(COFF)  - Loads initial data from Django fixtures"
	@echo -e "$(CYAN)make load-many-posts$(COFF)  - Loads many blog posts"
	@echo -e "$(CYAN)make superuser$(COFF)        - Runs django's createsuperuser command in the production container"
	@echo -e "$(CYAN)make superuser-dev$(COFF)    - Runs django's createsuperuser command in the development container"
	@echo -e "$(RED)make shutdown$(COFF)         - Shuts down the running services in production"
	@echo -e "$(RED)make shutdown-dev$(COFF)     - Shuts down the running services in development"
	@echo -e "$(RED)make shutdown-volumes$(COFF) - Shuts down the running services and deletes volumes in production"
	@echo -e "$(RED)make shutdown-volumes-dev$(COFF) - Shuts down the running services and deletes volumes in development"
	@echo -e "$(CYAN)make logs$(COFF)             - Shows server logs"
	@echo -e "$(CYAN)make logs-dev$(COFF)         - Shows server logs in development"
	@echo -e "$(CYAN)make logs-interactive$(COFF) - Shows interactive server logs"
	@echo -e "$(CYAN)make logs-interactive-dev$(COFF) - Shows interactive server logs in development"
	@echo -e "$(CYAN)make coverage-django$(COFF)  - Runs automatic code coverage check for Python"
	@echo -e "$(CYAN)make lint$(COFF)             - Runs code quality check for Python"
	@echo -e "$(CYAN)make lint-fix$(COFF)         - Fixes code quality for Python in entire project"
	@echo -e "$(CYAN)make test-project$(COFF)     - Runs automatic tests on the entire project"
	@echo -e "$(CYAN)make test-website$(COFF)     - Runs automatic tests on website app"
	@echo -e "$(CYAN)make test-users$(COFF)       - Runs automatic tests on users app"


shell:
	@echo -e "$(CYAN)Starting Django shell prompt:$(COFF)"
	@docker-compose -f docker-compose-prod.yml run --rm web python ./manage.py shell

shell-dev:
	@echo -e "$(CYAN)Starting Django shell prompt in development:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py shell

build:
	@echo -e "$(CYAN)Building website images:$(COFF)"
	@docker-compose -f docker-compose-prod.yml build

build-dev:
	@echo -e "$(CYAN)Building website images for development:$(COFF)"
	@docker-compose -f docker-compose-dev.yml build

runserver:
	@echo -e "$(GREEN)Starting Docker container with the app$(COFF)"
	@docker-compose -f docker-compose-prod.yml up -d
	@echo -e "$(CYAN)App ready and listening at http://127.0.0.1.$(COFF)"

runserver-dev:
	@echo -e "$(GREEN)Starting Docker container with the app in development.$(COFF)"
	@docker-compose -f docker-compose-dev.yml up -d
	@echo -e "$(CYAN)App ready and listening at http://127.0.0.1:8000.$(COFF)"

makemigrations:
	@echo -e "$(CYAN)Running django makemigrations:$(COFF)"
	@docker-compose -f docker-compose-prod.yml run --rm web python ./manage.py makemigrations $(cmd)

makemigrations-dev:
	@echo -e "$(CYAN)Running django makemigrations for development:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py makemigrations $(cmd)

collectstatic:
	@echo -e "$(CYAN)Running django collectstatic:$(COFF)"
	@docker-compose -f docker-compose-prod.yml run --rm web python ./manage.py collectstatic --no-input $(cmd)

collectstatic-dev:
	@echo -e "$(CYAN)Running django collectstatic in develoment:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py collectstatic $(cmd)

migrate:
	@echo -e "$(CYAN)Running django migrations:$(COFF)"
	@docker-compose -f docker-compose-prod.yml run --rm web python ./manage.py migrate $(cmd)

migrate-dev:
	@echo -e "$(CYAN)Running django migrations in development:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py migrate $(cmd)

load-initial-data:
	@echo -e "$(CYAN)Populating initial data from Django fixtures:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py loaddata website/fixtures/initial.json

load-many-posts:
	@echo -e "$(CYAN)Loading lots of blog posts:$(COFF)"
	@docker-compose run --rm web python ./manage.py loadmanyprojects $(cmd)

superuser:
	@echo -e "$(CYAN)Creating superuser:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py createsuperuser $(cmd)

superuser-dev:
	@echo -e "$(CYAN)Creating superuser:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python ./manage.py createsuperuser $(cmd)

shutdown:
	@echo -e "$(CYAN)Stopping services:$(COFF)"
	@docker-compose -f docker-compose-prod.yml down

shutdown-dev:
	@echo -e "$(CYAN)Stopping services:$(COFF)"
	@docker-compose -f docker-compose-dev.yml down

shutdown-volumes:
	@echo -e "$(CYAN)Stopping services and deleting volumes:$(COFF)"
	@docker-compose -f docker-compose-prod.yml down --volumes

shutdown-volumes-dev:
	@echo -e "$(CYAN)Stopping services and deleting volumes:$(COFF)"
	@docker-compose -f docker-compose-dev.yml down --volumes

logs:
	@echo -e "$(CYAN)Checking logs:$(COFF)"
	@docker-compose -f docker-compose-prod.yml logs

logs-dev:
	@echo -e "$(CYAN)Checking logs:$(COFF)"
	@docker-compose -f docker-compose-dev.yml logs

logs-interactive:
	@echo -e "$(CYAN)Checking logs interactively:$(COFF)"
	@docker-compose -f docker-compose-prod.yml logs -f

logs-interactive-dev:
	@echo -e "$(CYAN)Checking logs interactively:$(COFF)"
	@docker-compose -f docker-compose-dev.yml logs -f

coverage-django:
	@echo -e "$(CYAN)Running automatic code coverage check for Python:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web sh -c "coverage run -m py.test && coverage html && coverage report"

lint:
	@echo -e "$(CYAN)Running Black check:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web black --check .

lint-fix:
	@echo -e "$(CYAN)Running Black formatting:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web black .

test-project:
	@echo -e "$(CYAN)Running all automatic django tests:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python manage.py test

test-website:
	@echo -e "$(CYAN)Running automatic django tests on website app:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python manage.py test website.tests

test-users:
	@echo -e "$(CYAN)Running automatic django tests on users app:$(COFF)"
	@docker-compose -f docker-compose-dev.yml run --rm web python manage.py test users.tests
