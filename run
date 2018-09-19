#!/bin/bash

if [[ ! -d venv ]] ; then 
  echo "Detected there is not Virtualenv for this project"
  echo "Try to install virtualenv package"
  pip3 install virtualenv > /dev/null 
  echo "Create a virtualenv "
  virtualenv venv -p `which python3` > /dev/null 
fi;

# get into the virtual env
source venv/bin/activate

echo "Update the Software in Virtualenv"
# update the prerequiste
pip install -r ScriptDependency/requirements.txt > /dev/null


if [[ "$1" == "-f" || ! -e "db.sqlite3" ]] ;then
  # create a new database
  rm db.sqlite3 -rf

  echo "Create New Databsae"
  ./manage.py migrate >/dev/null

  echo "Import Basic Data"
  ScriptDependency/import_data.sh &

  echo "Create Super User"
  ./manage.py createsuperuser
fi;

echo "running the server"
./manage.py runserver
