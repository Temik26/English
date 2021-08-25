FROM python:latest

ENV PYTHONUNBUFFERED=1

COPY backend /code

WORKDIR /code

RUN pip install -r requirements.txt
