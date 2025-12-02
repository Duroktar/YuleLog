#!/usr/bin/env bash

CONTAINER_NAME=yule_log

docker build -t yule_log-dev --rm -f dockerfile.dev .
docker run -it --name yule_log_app-dev --rm yule_log-dev
