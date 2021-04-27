FROM python:alpine
WORKDIR /app
COPY . .
RUN apk add socat
RUN pip install -U pip
RUN pip install termcolor
EXPOSE 31337
ENTRYPOINT socat tcp-l:31337,reuseaddr,fork,crlf exec:"python app.py",pty,ctty,echo=0
