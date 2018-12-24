FROM python:3.5-slim

RUN mkdir -p /home/project/app

COPY . /home/project/app

WORKDIR /home/project/app

RUN pip install pipenv\
  &&  pipenv install --system --deploy --ignore-pipfile



