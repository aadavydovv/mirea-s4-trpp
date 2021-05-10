# syntax=docker/dockerfile:1

FROM python:buster

WORKDIR /workdir

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app src/travel_assistant
COPY docs docs
COPY pyproject.toml pyproject.toml
COPY setup.py setup.py
