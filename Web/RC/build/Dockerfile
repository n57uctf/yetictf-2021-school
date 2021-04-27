FROM python:3-alpine

RUN pip install flask
COPY ./app /app

WORKDIR /app
ENTRYPOINT [ "python3", "app.py" ]