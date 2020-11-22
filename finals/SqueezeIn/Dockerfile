FROM ubuntu:18.04
MAINTAINER nogag
RUN apt-get update
RUN apt-get install -y firefox python3.8 python3-pip
COPY geckodriver /usr/local/bin
COPY requirements.txt .
RUN pip3 install -r requirements.txt
WORKDIR /app
COPY src/ .
CMD [ "python3", "./app.py" ]