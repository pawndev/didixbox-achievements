FROM python:3.9

LABEL maintainer="pawndev <coquelet.c@gmail.com>"

COPY poetry.lock pyproject.toml /usr/src/app/

WORKDIR /usr/src/app/

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY . .

ENTRYPOINT poetry run bot

