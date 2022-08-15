# My Website Project

![image](https://user-images.githubusercontent.com/23359514/183810177-cfb570bf-2432-4625-a9d3-9a843735bc3d.png)

  ## Description
  This is a simple website that demonstrates web development using Django and Bootstrap and one that can be replicated
in various contexts such as personal portfolio and company websites. There is an accompanying free video tutorial thread for the approach used in writing the code and testing its working. It can be accessed 
[here]().

  ## Table of Contents
  - [Description](#description)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Licenses](#license)
  - [Contributing](#contributing)
  - [Tests](#tests)
  - [Deployment](#deployment)
  - [Questions](#questions)

  ## Installation
  This project components include Git, Docker, Python, Django and PostgreSQL therefore here is a list of their installation 
instructions.
### Software

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - Most common version control system.
  - [Docker Desktop Windows](https://docs.docker.com/desktop/windows/install/) - Software for handling development operations (DevOps). Installs Docker CLI, Docker Compose etc.
  - [Docker Desktop Linux](https://docs.docker.com/desktop/linux/install/) - Installs Docker CLI, Docker Compose etc.
  - [Postgres](https://hub.docker.com/_/postgres?tab=tags) - Database leveraged in this project. Version referenced in [docker-compose.yml](docker-compose-dev.yml)
  - [Python](https://www.python.org/downloads/release/python-3810/) - Core language used in this project. Version referenced in the [Dockerfile](Dockerfile)
  - [Django](https://docs.djangoproject.com/en/4.0/topics/install/) - Python web development framework for developers with deadlines. Version referenced in [Pipfile](Pipfile)

### Dependencies
  The project dependencies specific to Python include: __pipenv, django, psycopg2-binary, crispy-bootstrap5, django-allauth, django-ckeditor, pip, 
  whitenoise, pillow__ and [Pipfile](Pipfile) lists them.

### Procedure

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
  10. Please check the live website at **https://mywebsite-jkariukidev.herokuapp.com/**

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
