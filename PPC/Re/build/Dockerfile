FROM python:3-alpine

MAINTAINER by_sm

ADD ./app /app

WORKDIR /app

RUN apk add --no-cache socat
RUN chmod +x /app/run.sh /app/generate.py /app/flag.txt
RUN python3 -m pip install termcolor

ENTRYPOINT [ "sh", "run.sh" ]
