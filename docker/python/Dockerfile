FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /server
COPY . /server
WORKDIR /server

ADD requirements.txt /server
RUN pip install -r requirements.txt
ADD . /server/