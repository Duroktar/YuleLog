FROM python:3.6-slim

RUN useradd --create-home --shell /bin/bash app_user

RUN apt-get -y update && apt-get install -y zlib1g-dev
RUN apt-get -y update && apt-get install -y libjpeg-dev
RUN apt-get -y update && apt-get install -y gcc

ENV LDFLAGS=-L/usr/lib/x86_64-linux-gnu/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install YuleLog

USER app_user
CMD [ "YuleLog" ]
