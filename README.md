# SENG2011

Using django, Vue.js, vuetifyjs

## Getting involve

### Set Your Working Branch

```shell
# create to your branch and working there
$ git checkout -b YOUR_BRANCH_NAME

# when you finshish, push the commits
$ git add && git commmit && git push
# IF you are push this branch FIRST TIME, you may use this line
$ git push --set-upstream origin YOUR_BRANCH_NAME
```

### Setting Environment

Make sure you have install these package in your package manager:  
python3, python3-venv, virtualenv

```shell
# in Ubuntu 
sudo apt install python3 python3-venv virtualenv 
```


```shell
# Create Virtual environment if you haven't
$ virtualenv venv -p `which python3` 
```

```shell
# activate the virtual envirnoment
$ source venv/bin/activate
```

### Install dependencies and setup the database

```shell
(venv) $ pip install -r requirements.txt

# setup the database
(venv) $ ./init_db.sh
```

### Run the Server

A shell to run django's httpd.

```shell
# Run in local
(venv) $ ./manage.py runserver

# ALTERNATIVE: start the server to public
(venv) $ sudo python manage.py runserver 0:80
```

### Install frontend dependencies and run the Web

```shell
Tobe added
```

## URLs

### Frontend

# partywhip-frontend

> the frontend project of partywhip

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

### Backend

URL | Detail
:--- | :---
http://127.0.0.1:8000/admin | Django admin
http://127.0.0.1:8000/api-v0/ | Index of party whip's api  
http://127.0.0.1:8000/ | Index of party whip's  
