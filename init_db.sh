#!/bin/bash

# get into the virtual env  
source venv/bin/activate 

echo "Update the Software in Virtualenv"
# update the prerequiste 
pip install -r requirements.txt > /dev/null 


# create a new database 
rm db.sqlite3 -rf 

echo "Create New Databsae"
./manage.py migrate >/dev/null 

echo "Create Super User"
./manage.py createsuperuser 

echo "Import Basic Data"
./manage.py shell < init_data.py &