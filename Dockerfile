FROM python:3.9

WORKDIR /app/

ENV PYTHONUNBUFFERED 1

COPY req.txt /app/

COPY . /app/

RUN pip install --no-cache-dir -r /app/req.txt && python3 manage.py collectstatic

RUN python3 manage.py makemigrations