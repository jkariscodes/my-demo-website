# Example FullStack Web Project

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
  This is a simple website that demonstrates full-stack web development using Django and Vanilla JavaScript, CSS and HTML and one that can be replicated in various contexts such as personal portfolio and other websites. There is an accompanying free video tutorial thread for the approach used in writing the code and testing its working. It can be accessed [here](https://bit.ly/3HXmdLd).

  ## Installation
  This project's software components include:
  * **Git**
  * **Docker & Docker Compose**
  * **Python** 
  * **Django**
  * **PostgreSQL**

### Software

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - Used for version control in development of this project.
  - [Docker Desktop Windows](https://docs.docker.com/desktop/windows/install/) - Software for handling development operations (DevOps) using graphical user interface (GUI) in Windows. Installs Docker Command Line Interface, Docker Compose etc.
  - [Docker Desktop Linux](https://docs.docker.com/desktop/linux/install/) - Software for handling development operations (DevOps) using graphical user interface (GUI) in Linux.
  - [Postgres](https://hub.docker.com/_/postgres?tab=tags) - Object Relational Database Management System used to store and support DB operations in this project. Specific version is referenced in [development](docker-compose-dev.yml) and [production](docker-compose-dev.yml) configurations.
  - [Python](https://www.python.org/downloads/release/python-3810/) - Core programming language used in the development of this project. Specific version is referenced in the [development](Dockerfile-dev) and [production](Dockerfile) build configurations.
  - [Django](https://docs.djangoproject.com/en/4.0/topics/install/) - Python web development framework that is the main framework used in this project.

### Dependencies
The back-end consists of a Docker container with Python and Django. This project's initial dependencies are listed in the [Pipfile](Pipfile) include: 
* [__Django__](https://docs.djangoproject.com/) as the base framework
* [__django-environ__](https://django-environ.readthedocs.org/) for management of environment variables
* [__markdown__](http://pythonhosted.org/Markdown/siteindex.html) for rendering markdown in HTML
* [__psycopg__](https://www.psycopg.org/docs/) database adapter to facilitate database connectivity and other operations.
* [__psycopg-binary__](https://www.psycopg.org/docs/) database adapter to facilitate database connectivity and other operations.
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
* [__black__](https://github.com/psf/black) for linting and automatically formatting the code during development
* [__pytest__](https://docs.pytest.org/en/latest/) for writing tests
* [__Django Debug Toolbar__](https://django-debug-toolbar.readthedocs.io/) to help with debugging during development
* [__Faker__](https://faker.readthedocs.io) for generating fake data for use/test in this project (TODO)
* [__coverage__](https://coverage.readthedocs.io/) for measuring code coverage
* [__pytest-django__](https://pytest-django.readthedocs.io/) for testing django specific functionalities during development (TODO)
* [__django-csp__](https://django-csp.readthedocs.io/) for implementing Content Security Policy in this project.

### Deployment
The minimum requirements required to deploy this project is [Docker Engine](). Docker Engine contains docker, [docker compose]() and if on a Desktop environment and prefer a graphical user interface, once can make use of [Docker Desktop]().
#### Local
1. Clone the repository via commandline by executing `git clone https://github.com/jkariukidev/my-demo-website.git`
2. Create the environment variables file from the provided [development sample file](.env_dev.sample). You should now have the `.env` file required by docker-compose.
3. Edit the environment variables accordingly. They include:
   * ``PROJECT_ENV`` - The project environment state. Set this to development in your local machine setup.
   * ``SECRET_KEY`` - Django cryptography key described in detail [here](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key).
   * ``DEBUG`` - Variable used in fixing issues in development (hence set to ``True`` in development) and should never be set to ``True`` in 
       production. [Reference](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/#debug)
   * ``ALLOWED_HOSTS`` - List of host/domain names that this Django site can serve.
   * ``ENGINE`` - Database backend to use. This project uses PostgreSQL backend by default but can be changed in the environment variables.
   * ``DB_NAME`` - Database to be used by this application.
   * ``DB_USER`` - Database user/role to be used by this application.
   * ``DB_PASSWORD`` - Password for the user defined by `DB_USER`.
   * ``DB_HOST`` - Host of the database server. Defined in the docker-compose files as `database` service.
   * ``DB_PORT`` - Network port used by the database also defined in the docker-compose files.
   * ``EMAIL_BACKEND`` - The backend to use for sending emails set to `console` in development. Details are well illustrated [here](https://docs.djangoproject.com/en/4.1/topics/email/).
   * ``POSTGRES_DB`` - Postgres database name defined in docker-compose files. [postgresql reference](https://www.postgresql.org/docs/14/libpq-envars.html), [docker reference](https://hub.docker.com/_/postgres)
   * ``POSTGRES_USER`` - Optional variable used together with ``POSTGRES_PASSWORD`` that sets a user and password. Also defined in docker-compose files.
   * ``POSTGRES_PASSWORD`` - Mandatory variable used to set a superuser password. Must not be empty. Also defined in docker-compose files.
   
4. Build the required docker images for development by executing `make build-dev`
5. Run the docker containers by executing `make runserver-dev`
6. Apply migrations to synchronize the database state with the current set of models and migration using `make migrate-dev`
7. Load initial data, creating test user account, blog category and blog posts making use of [django fixtures](https://docs.djangoproject.com/en/4.1/howto/initial-data/) and referred to in [initial.json](website/fixtures/initial.json) file.
   `make load-initial-data` creates sample blog posts, a superuser, and a test user. To see this change, please refresh your browser in the articles page. 
8. Create superuser (optional) by executing `make superuser-dev`
9. To log into admin panel, use the details below:
    * URL: http://localhost:8000/tajiri (local environment)
    * Username: `webadmin`
    * Password: `IAmTheAdmin123`
10. Check logs using `make logs-dev` or to view the logs interactely use `make logs-interactive-dev`

#### Production
  1. Clone this project using `git clone ` command.
      ```shell
     git clone https://github.com/jkariukidev/my-demo-website.git
     ```
  2. Navigate into the cloned project folder and using a terminal/shell or otherwise, rename the [env_prod.sample](.env_prod.sample) to `.env` in production to be recognized by docker compose.
  3. Edit the environment variables as required and ensure you do not share passwords and secure keys with the public. The additional environment variables for production include:
     * ``PROJECT_ENV`` - The project environment state. Set this to production in your in public server host.
     * ``USE_S3`` - Tells Django whether to use AWS S3 bucket for static file management which brings about additional variables defined [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html). AWS account is required. Read more about [AWS S3](https://docs.aws.amazon.com/s3/).
     * ``EMAIL_BACKEND`` - This is the backend to use for email. Django supports various  [email backends](https://docs.djangoproject.com/en/4.1/topics/email/#topic-email-backends).
     * ``DEFAULT_FROM_EMAIL`` - The default email to use from this site's manager. 
     * ``EMAIL_HOST`` - This is the host to use for sending email.
     * ``EMAIL_HOST_USER`` - The username for the sending service / SMTP defined in the ``EMAIL_HOST``
     * ``EMAIL_HOST_PASSWORD`` - The password for the user for sending service / SMTP defined in the ``EMAIL_HOST``
     * ``EMAIL_PORT`` - The port to use for the email sending service.
     * ``EMAIL_USE_TLS`` - This tells the project whether to use secure protocol (port 587) when communicating with email sending service.
     
  4. Run the docker services for this project using compose in production environment.
     ```
     make runserver
     ```
  5. Propagate models into your database schema using the [migrate command](https://docs.djangoproject.com/en/4.0/ref/django-admin/#migrate). Note
     that this command is being run inside the docker web container. Refer for more on [exec docker command](https://docs.docker.com/engine/reference/commandline/compose_exec/).
     ```
     make migrate
     ```
  6. Check logs using `make logs` or to view the logs interactively use `make logs-interactive`

For several other commands, view them in the [Makefile](Makefile)


  ## Usage

  - Developing and deploying a modern website
  - Personal blog article management
  - User account management including authentication and authorization extensibility.
  - Emailing and web form security
  - REST API

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
 - Implementation of Django Unittest in this project. Run the tests using:
   * ``make test-project`` - To run all automatic django tests for the entire project.
   * ``make test-website`` - To run all automatic django tests for the website app only.
   * ``make test-users`` - To run all automatic django tests for the users app only.
 - Other testing tools that cab be incorporated here include:
   * [Tox](https://docs.djangoproject.com/en/4.0/internals/contributing/writing-code/unit-tests/#running-tests-using-tox)
   * [Django testing tools](https://docs.djangoproject.com/en/4.0/topics/testing/tools/)
 
 Some of the packages that help in testing include:
   * ``Django-Debug-Toolbar`` which by default appears on the test/development deployment as shown.
   ![image](https://user-images.githubusercontent.com/23359514/222653944-16ca0957-582d-42db-8d20-f4d7de68fedd.png)



## Deployment
Use the [production configuration](docker-compose-prod.yml) in deploying into a public server. Following the guidelines on deployment in tutorial demo:
- [Video Tutorial Demo](https://www.youtube.com/playlist?list=PLIET7uEHqcqif6wye0sL-XZ9o95zgYmaa)

## Questions
If you have any questions you can contact me!

- [My Socials](https://linktr.ee/josephkariuki)
- [My Website](https://josephkariuki.com)

## References
- [Django Documentation](https://docs.djangoproject.com/)
- [Learn Django](https://learndjango.com/)
- [Docker Documentation](https://docs.docker.com/)
