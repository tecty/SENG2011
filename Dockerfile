FROM python:3-onbuild

ADD requirements.txt /usr/src/app
WORKDIR /usr/src/app

