FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY src/requirements.txt .

RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt

COPY /src/alembic ./alembic
COPY /src/app ./app
COPY /src/alembic.ini .