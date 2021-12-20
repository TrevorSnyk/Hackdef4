FROM python:3.10.0b2
MAINTAINER @nogagmx
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src/ .
CMD [ "python", "./app.py" ]