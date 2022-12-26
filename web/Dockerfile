FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN mkdir /web_django
COPY requirements.txt /web_django/
WORKDIR /web_django

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /web_django/

