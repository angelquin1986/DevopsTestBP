#author angel quingaluisa
# archivo docker para crear una imagen donde se aloga nuestra app
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
