FROM python:3.9

WORKDIR /app/

ENV PYTHONUNBUFFERED 1

COPY req.txt /app/

RUN pip install -r /app/req.txt

COPY . /app/