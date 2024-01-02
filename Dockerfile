FROM python:3.9-slim

RUN mkdir /work
WORKDIR /work

COPY main.py /work

ENTRYPOINT python -u main.py
