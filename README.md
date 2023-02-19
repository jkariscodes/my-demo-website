# Example Website Project

![image](https://user-images.githubusercontent.com/23359514/183810177-cfb570bf-2432-4625-a9d3-9a843735bc3d.png)

## Table of Contents
  - [Description](#description)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Licenses](#license)
  - [Contributing](#contributing)
  - [Tests](#tests)
  - [Deployment](#deployment)
  - [Questions](#questions)

  ## Description
  This is a simple website that demonstrates web development using Django and Bootstrap and one that can be replicated in various contexts such as personal portfolio and company websites. There is an accompanying free video tutorial thread for the approach used in writing the code and testing its working. It can be accessed [here](https://bit.ly/3HXmdLd).

  ## Installation
  This project's software components include:
  * Git
  * Docker & Docker Compose
  * Python 
  * Django
  * PostgreSQL

### Software

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - Used for version control in development of this project.
  - [Docker Desktop Windows](https://docs.docker.com/desktop/windows/install/) - Software for handling development operations (DevOps) using graphical user interface (GUI) in Windows. Installs Docker Command Line Interface, Docker Compose etc.
  - [Docker Desktop Linux](https://docs.docker.com/desktop/linux/install/) - Software for handling development operations (DevOps) using graphical user interface (GUI) in Linux.
  - [Postgres](https://hub.docker.com/_/postgres?tab=tags) - Object Relational Database Management System used to store and support DB operations in this project. Specific version is referenced in [docker-compose.yml](docker-compose-dev.yml)
  - [Python](https://www.python.org/downloads/release/python-3810/) - Core programming language used in the development of this project. Specific version is referenced in the [Dockerfile](Dockerfile)
  - [Django](https://docs.djangoproject.com/en/4.0/topics/install/) - Python web development framework that is the main framework used in this project.

### Dependencies
The back-end consists of a Docker container with Python and Django. This project's initial dependencies are listed in the [Pipfile](Pipfile) include: 
* [__Django__](https://docs.djangoproject.com/) as the base framework
* [__django-environ__](https://django-environ.readthedocs.org/) for management of environment variables
* [__markdown__](http://pythonhosted.org/Markdown/siteindex.html) for rendering markdown in HTML
* [__psycopg2-binary__](https://www.psycopg.org/docs/) database adapter to facilitate database connectivity and other operations.
* [__crispy-bootstrap5__](https://github.com/django-crispy-forms/crispy-bootstrap5) Bootstrap5 template pack for django-crispy-forms.
* [__django-allauth__](https://django-allauth.readthedocs.io/en/latest/) reusable Django app that allows for both local and social authentication
* [__django-ckeditor__](https://github.com/django-ckeditor/django-ckeditor) providing editor support in the project.
* [__whitenoise__](https://github.com/evansd/whitenoise) for managing static and user uploads in developement and production
* [__pillow__](https://python-pillow.org/) for supporting image processing and capabilities. 
* [__gunicorn__](https://gunicorn.org/) HTTP server for supporting serving of this project over the web
* [__dj-database-url__](https://github.com/jazzband/dj-database-url) support for database URL environment variable
* [__boto3__](https://github.com/boto/boto3) supporting Amazon's S3 capabilities
* [__django-storages__](https://github.com/jschneier/django-storages) support for Amazon's S3 storage backend. Can be used with other storage backends e.g. Digital Ocean, DropBox, Google Cloud etc. 
* [__djangorestframework__](https://www.django-rest-framework.org) for provision of WebAPI and REST capabilities
* [__black__](https://github.com/psf/black) for linting and automatically formatting the code
* [__pytest__](https://docs.pytest.org/en/latest/) for writing tests
* [__Django Debug Toolbar__](https://django-debug-toolbar.readthedocs.io/) to help with debugging
* [__Faker__](https://faker.readthedocs.io) for generating fake data for use/test in this project
* [__coverage__](https://coverage.readthedocs.io/) for measuring code coverage during testing
* [__pytest-django__](https://pytest-django.readthedocs.io/) for testing django specific functionalities

### Deployment
The minimum requirements required to deploy this project is [Docker Engine](). Docker Engine contains docker, [docker compose]() and if on a Desktop environment and prefer a graphical user interface, once can make use of [Docker Desktop]().
#### Local
1. Clone the repository via commandline by executing `git clone `
2. Create the environment variables file from the provided [development sample file](.env_dev.sample). You should now have the `.env_dev.yml` file.
3. Edit the environment variables accordingly. They include environment, secret key, database connection settings etc.
4. Build the required docker images by executing `make build-dev`
5. Run the docker containers by executing `make up-dev`
6. Create super user (optional) by executing `make superuser-dev`

#### Production
  To launch the project, follow the following steps.
  1. Install Git, Python with Pipenv (Pip can also be used), and Docker. Take note of [Windows pre-requisites](https://docs.docker.com/desktop/windows/install/#system-requirements) 
     and [Linux pre-requisites](https://docs.docker.com/desktop/linux/install/#system-requirements) of installing Docker priorto proceeding.
  2. Clone this project using `git clone` command.
      ```shell
     git clone https://github.com/jkariukidev/my-demo-website.git
     ```
  3. Navigate into the cloned project folder and using a terminal/shell or otherwise, rename the [.env_dev.sample](.env_dev.sample) 
     or [env_prod.sample](.env_prod.sample) to `.env_dev` in development or `.env_prod` in production to be recognized by docker compose.
  4. Edit the environment variables as you please and ensure you do not share passwords and secure keys with the public. The env variables include:
     - ``SECRET_KEY`` - Django cryptography key leveraged in [reference](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key).
     - ``POSTGRES_DB`` - Postgres database name. [postgresql reference](https://www.postgresql.org/docs/14/libpq-envars.html), [docker reference](https://hub.docker.com/_/postgres)
     - ``POSTGRES_USER`` - Optional variable used together with ``POSTGRES_PASSWORD`` that sets a user and password.
     - ``POSTGRES_PASSWORD`` - Mandatory variable used to set a superuser password. Must not be empty.
     - ``DEBUG`` - Variable used in fixing issues in development (hence set to ``False``)environment and should never be set to ``True`` in 
       production. [Reference](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/#debug)
  5. Run the docker services for this project using compose in development environment.
     ```
     docker compose -f docker-compose-dev.yml up
     ```
     OR to run in a detached mode (without seeing the logs) .ie. in the background
     ```
     docker compose -f docker-compose-dev.yml up -d
     ```
  6. Run the docker services for this project using compose in production environment.
     ```
     docker compose -f docker-compose-prod.yml up
     ```
     OR to run in a detached mode (without seeing the logs) .ie. in the background
     ```
     docker compose -f docker-compose-prod.yml up -d
     ```
  7. Propagate models into your database schema using the [migrate command](https://docs.djangoproject.com/en/4.0/ref/django-admin/#migrate). Note
     that this command is being run inside the docker web container. Refer for more on [exec docker command](https://docs.docker.com/engine/reference/commandline/compose_exec/).
     ```
     docker compose -f docker-compose-dev.yml exec web python manage.py migrate
     ```
     similarly, in production
     ```
     docker compose -f docker-compose-dev.yml exec web python manage.py migrate
     ```
  8. To check the logs you can make use of ``docker compose -f docker-compose-dev.yml logs`` or ``docker compose -f docker-compose-dev.yml logs -f`` to continue watching the log file and its print out.
  9. In development, access the website in (HTTP) http://localhost:8000 while in production, (HTTPS) https://localhost

  ## Usage

  - Developing and deploying a modern website
  - Personal blog article management
  - User account management including authentication and authorization extensibility.
  - Emailing and web form security

  ## License
  - [LICENSE](LICENSE)

  ## Contributing
  If you want to contribute to a project and make it better, your help is very welcome. Contributing is also a great 
  way to learn more about social coding on GitHub, new technologies and their ecosystems and how to make constructive, 
  helpful bug reports, feature requests and the noblest of all contributions: a good, clean pull request.

### making clean pull request

Look for a project's contribution instructions. If there are succinct, please follow them.

- Create a personal fork of the project on GitHub by clicking [here](https://github.com/jkariukidev/my-demo-website/fork).
- Clone the fork on your local machine. Your remote repo on GitHub is called `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into your local repository.
- Create a new branch to work on! Branch from `develop` if it exists, else from `master`.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- If the project has tests run them!
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Squash your commits into a single commit with git's [interactive rebase](https://help.github.com/articles/interactive-rebase). 
  Create a new branch if necessary.
- Push your branch to your fork on GitHub, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's `develop` branch if there is one, else 
  go for `master`!

- If the maintainer requests further changes just push them to your branch. The PR will be updated automatically.
- Once the pull request is approved and merged you can pull the changes from `upstream` to your local repo and delete
your extra branch(es).

And last but not least: Always write your commit messages in the present tense. Your commit message should describe what 
the commit, when applied, does to the code – not what you did to the code.

  ## Tests
  Following the guidelines on testing Python projects using:
  - Implementation of Django Unittest in this [test.py](website/tests.py) file. Run the tests using ``docker compose -f docker-compose-dev.yml exec web python manage.py test``
  - [Tox](https://docs.djangoproject.com/en/4.0/internals/contributing/writing-code/unit-tests/#running-tests-using-tox)
  - [Django testing tools](https://docs.djangoproject.com/en/4.0/topics/testing/tools/)

  ## Deployment
  Use the [production configuration](docker-compose-prod.yml) in deploying into a public server. Following the guidelines on deployment in tutorial demo:
  - [Demo](https://youtube.com/josephkariukidev)

  ## Questions
  If you have any questions you can contact me!

  - [My Socials](https://linktr.ee/josephkariuki)
  - [My Website](https://josephkariuki.com)
  ## References
  - [Django Documentation](https://docs.djangoproject.com/)
  - [Learn Django](https://learndjango.com/)
