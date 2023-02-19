# Base image

FROM python:3.10.6-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# Working directory

WORKDIR /website

# Installing dependencies

COPY Pipfile Pipfile.lock /website/

RUN pip install pipenv && pipenv install --system

# Copy project files and directories

COPY . /website/
