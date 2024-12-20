FROM mcr.microsoft.com/devcontainers/python:3.13

WORKDIR /computation_and_information

COPY . .

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install -y aspell

RUN pipenv install
