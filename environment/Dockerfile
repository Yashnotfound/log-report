FROM python:3.13-slim-bookworm@sha256:e09fe4e2f53ffae8fb7cadf60efc16a443fc34d5bb72a9348ab538c9d4a24d80

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
