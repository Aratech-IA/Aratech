FROM python:3.12-alpine

RUN apk add mlocate nano gettext build-base python3-dev bash

RUN pip install django==5.1.4 psycopg2-binary uvicorn==0.22.0 django_compressor websockets django-libsass django-sass-compiler requests

RUN sed -i  '/config.should_reload:/a  \ \ \ \ \ \ \ \ server.force_exit = True' /usr/local/lib/python3.12/site-packages/uvicorn/main.py

WORKDIR /App

COPY ./src .

RUN chmod +x start.sh asgi.sh
