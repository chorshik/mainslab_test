FROM python:3.10-slim-buster
WORKDIR /src
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql python-psycopg2 libpq-dev\
  && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
COPY . /src