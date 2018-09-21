FROM python:3

WORKDIR /usr/src/app
ADD requirements.txt .
# install the pip requirements 
RUN pip install -r requirements.txt


# run the prerequesite install again, 
# since we may change the requirement list during development 
CMD ./run
