FROM python:3-alpine
WORKDIR /app
COPY . .
RUN apk add socat
EXPOSE 1234
ENTRYPOINT socat tcp-l:1234,reuseaddr,fork,crlf exec:"python enc.py",pty,ctty,echo=0
