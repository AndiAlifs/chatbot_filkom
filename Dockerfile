# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /chatbot-filkom

COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install libmariadbclient-dev --Yes gcc --Yes

RUN pip install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0:5000"]