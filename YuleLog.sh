#!/usr/bin/env bash

CONTAINER_NAME=yule_log
VERSION=0.0.3-docker-2

if [[ $(docker images $CONTAINER_NAME:$VERSION | grep -w "$CONTAINER_NAME") ]]; then
    echo "docker-run ..."
    docker run -it --name yule_log_app --rm yule_log:$VERSION

else
    echo "docker-build ..."
    docker build -t yule_log:$VERSION .
    docker run -it --name yule_log_app --rm yule_log:$VERSION
fi
