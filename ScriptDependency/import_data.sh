#!/usr/bin/env bash
<<COMMENT
  This script can be only call by init.sh or use 
  ScriptDependency/import_data.sh
  to run it 
COMMENT


# this script need to get into virtual env
source venv/bin/activate


for file in ScriptDependency/*_data.py ; do
  # use concurrency to import all the data file has written
  ./manage.py shell < $file 
done
