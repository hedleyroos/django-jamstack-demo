# syntax = docker/dockerfile:experimental
FROM python:3.7.11-buster
WORKDIR /var/app

#RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y vim

COPY requirements.txt /var/app/
COPY manage.py /var/app/
COPY wsgi.py /var/app/
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip python -m pip install -r /var/app/requirements.txt
COPY sample.sqlite3 /var/app/db.sqlite3
COPY jamstack /var/app/jamstack

EXPOSE 80
ENTRYPOINT sleep 1 && yes 'yes' | python manage.py distill-local /tmp/jamstack/ --force --collectstatic && cp -r /tmp/jamstack/* /var/tmp/jamstack && uwsgi --http :80 --callable application --wsgi-file wsgi.py
