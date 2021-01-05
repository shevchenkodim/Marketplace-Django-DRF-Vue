FROM python:3.9-alpine as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/usr/src/syms_marketplace

RUN mkdir $APP_HOME $APP_HOME/staticfiles $APP_HOME/mediafiles
WORKDIR $APP_HOME

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev\
    && apk add --update --no-cache g++ gcc libxml2-dev libxslt-dev libffi-dev openssl-dev make\
    && pip install psycopg2 \
    && pip install --upgrade pip\
    && pip3 install -U lazy-object-proxy==1.4.3

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . $APP_HOME/
