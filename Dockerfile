# syntax=docker/dockerfile:1
FROM python:3.12.4-alpine3.20
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/django
COPY requirements.txt ${WORKDIR}
RUN apk update \
    && apk add libmagic \
    && pip install -r requirements.txt
COPY . ${WORKDIR}
