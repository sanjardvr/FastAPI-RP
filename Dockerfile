FROM python:3.10 as base

ARG env

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export $(test "${env:-dev}" != "prod" && echo "--with dev") \
    -f requirements.txt \
    --output requirements.txt \
    --without-hashes

FROM python:3.10

COPY --from=base /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

ADD . /app/
WORKDIR /app
ENV PYTHONPATH=/app

EXPOSE 8888
