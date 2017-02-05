FROM ubuntu
MAINTAINER Chat do CAOS  <chatcaos@gmail.com>

RUN groupadd web
RUN useradd -d /home/caos -m caos

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install python-pip -y
ADD server.py /home/caos/server.py
RUN pip install bottle

EXPOSE 8085
ENTRYPOINT ["/usr/bin/python", "/home/caos/server.py"]
USER caos
