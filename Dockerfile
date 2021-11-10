FROM python:3

WORKDIR /code

RUN apt-get update
RUN apt-get -y install vim

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
