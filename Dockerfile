# syntax=docker/dockerfile:1.4
FROM python:3.11-slim


WORKDIR /srv/flask_app

RUN apt-get clean \
    && apt-get -y update



RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

COPY requirements.txt /srv/flask_app/requirements.txt

RUN pip install -r requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx

COPY . /srv/flask_app

RUN chmod +x ./start.sh
EXPOSE 8080
CMD ["./start.sh"]
