FROM python:3
MAINTAINER Ram Durairajan "noemail@website.domain"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /appp
WORKDIR /appp
RUN pip install -r requirements.txt
