FROM mcr.microsoft.com/devcontainers/python:3.13

WORKDIR /computation_and_information

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install -y aspell
    
COPY . .
    
RUN pipenv install
