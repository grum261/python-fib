FROM python:latest

ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN pip install pipenv
COPY Pipfile* /code/
RUN pipenv install --system --deploy --ignore-pipfile
COPY config /code/