FROM python:3.10-slim-buster
MAINTAINER Jonathan Finger

ENV INSTALL_PATH /sniffr_bot
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

RUN apt-get update
RUN apt-get -y install gcc

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD python main.python