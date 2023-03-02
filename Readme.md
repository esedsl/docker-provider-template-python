# Docker Provider Template

## Description

This is a template for a docker provider. It is a python3 application that can be run in a docker container. It is a simple express server that exposes a REST API to be used by the Petam.io platform.

## Requirements

- python 3.11
- docker

## Usage

```sh
curl --location --request GET '${URL_DEL_DOCKER}/?target_address=${TARGET_SCAN}' \
--header 'JWT: 123' \
--header 'webhook_url: ${URL_DE_RETORN}' 
# To test the docker provider locally you can use the following website https://requestcatcher.com/ to get the webhook_url
```

## Development proccess

1. modificar el fitxer provider.py amb la implementacio del proveidor
4. fer python main.py per testejar la implementacio
5. modificar el fitxer Dockerfile amb les dependencies necessaries per la imatge
6. docker build -t provider-name 
7. docker run --rm -p 8080:8080 provider-name
8. docker push per pujar la imatge al registry (Unicament desde ESED)

## Run app

### Run scripts localy

```sh
python main.py
```

### Run scripts in docker

```sh
docker build -t provider-name
docker run --rm -p 8080:8080 provider-name
```
