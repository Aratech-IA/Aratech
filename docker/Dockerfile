FROM python:3.10-bullseye

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y mlocate nano

RUN pip install django==4.2 psycopg2 uvicorn==0.22.0 django_compressor websockets django-libsass django-sass-compiler

RUN sed -i  '/config.should_reload:/a  \ \ \ \ \ \ \ \ server.force_exit = True' /usr/local/lib/python3.10/site-packages/uvicorn/main.py

WORKDIR /App

RUN git clone https://github.com/Aratech-IA/Aratech.git

CMD ["/App/Aratech/asgi.sh"]
