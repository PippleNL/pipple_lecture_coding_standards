FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ARG IMAGE_NAME=latest

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

ENV IMAGE_NAME=$IMAGE_NAME
