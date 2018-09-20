FROM python:3

ADD requirements.txt /usr/src/app
WORKDIR /usr/src/app
# install the pip requirements 
RUN pip install -r requirements.txt


# run the prerequesite install again, 
# since we may change the requirement list during development 
CMD ./run
