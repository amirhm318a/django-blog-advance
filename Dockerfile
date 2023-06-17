FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1



WORKDIR /app


COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./core /app

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

