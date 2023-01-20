FROM python:3.10

COPY app /app

RUN /usr/local/bin/python /app/__main__.py bdist

RUN ls -laR /app
