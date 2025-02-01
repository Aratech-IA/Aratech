FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential mlocate nano gettext python3-dev libffi-dev libsass-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install django==5.1.5 psycopg2-binary uvicorn==0.34.0 django_compressor websockets django-libsass django-sass-compiler requests

RUN sed -i  '/config.should_reload:/a  \ \ \ \ \ \ \ \ \ \ \ \ server.force_exit = True' /usr/local/lib/python3.12/site-packages/uvicorn/main.py

WORKDIR /App

COPY ./src .

RUN chmod +x start.sh asgi.sh
