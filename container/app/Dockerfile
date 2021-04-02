FROM python:3.7-slim-stretch

RUN apt-get update -y && apt-get install -y libzbar-dev bash gcc git libc-dev curl wget vim nano \
    && apt-get install -y ranger caca-utils highlight atool w3m poppler-utils mediainfo \
    && apt-get install -y iputils-ping telnet openssh-client net-tools \
    man unzip vim-tiny bc openssh-server thrift-compiler netcat sudo \
    && apt-get install -y build-essential \
    && apt-get autoremove -y \
    && apt-get clean

#Project
RUN apt-get update -y && apt-get install -qy graphviz \
    default-libmysqlclient-dev mongodb-clients mysql-client wget host

COPY container/app/requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf requirements.txt

COPY container/app/run.sh run.sh
RUN chmod a+rx run.sh

RUN mkdir -p /main
COPY ./src /main

RUN chmod -R a+rx /main
WORKDIR /main
