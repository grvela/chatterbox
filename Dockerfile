FROM python:3.7.2

COPY . /app

WORKDIR /app

RUN pip install -r requeriments.txt


