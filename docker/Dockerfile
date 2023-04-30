FROM python:3.10-bullseye

RUN apt update && DEBIAN_FRONTEND=noninteractive  apt install -y mlocate nano

RUN pip install django==4.2 psycopg2 uvicorn==0.22.0 django_compressor websockets django-libsass django-sass-compiler

RUN sed -i  '/config.should_reload:/a  \ \ \ \ \ \ \ \ server.force_exit = True' /usr/local/lib/python3.10/site-packages/uvicorn/main.py

WORKDIR /App
ADD "https://api.github.com/repos/aratech-IA/aratech/commits/main" latest_commit
RUN git clone https://github.com/Aratech-IA/Aratech.git
RUN cd Aratech && python manage.py collectstatic && python manage.py migrate

CMD ["/App/Aratech/asgi.sh"]
