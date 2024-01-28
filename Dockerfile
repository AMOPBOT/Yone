FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get -y update && apt-get -y install git gcc python3-dev ffmpeg tini

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/bin/tini", "--"]
RUN pip3 install pillow==9.5.0
CMD [ "python", "kora.py"]
