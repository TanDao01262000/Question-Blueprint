FROM python:3.10-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install gensim

ENV PYTHONUNBUFFERED=1

WORKDIR /app/qb/

COPY requirements.txt /app/qb/

RUN pip install -r requirements.txt

COPY . /app/qb/

# specified for the container host
EXPOSE 8888  

CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]

