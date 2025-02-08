FROM mcr.microsoft.com/devcontainers/python:3.13

WORKDIR /computation_and_information

COPY . .
    
RUN pipenv install
