FROM python:3-onbuild

COPY ScriptDependency/requirements.txt /usr/src/app
WORKDIR /usr/src/app

