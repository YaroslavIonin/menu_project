FROM python:3.10-slim

RUN mkdir /server
WORKDIR /server

COPY pyproject.toml /server

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY . /server
