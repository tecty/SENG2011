# SENG2011

PartyWhip Project Using:  
Frontend:
[Vue](https://cn.vuejs.org/v2/guide/),
[Vuex](https://vuex.vuejs.org/guide/),
[Vuetify](https://vuetifyjs.com/en/getting-started/quick-start),
[Vue-router](https://router.vuejs.org/),
[Axios](https://cn.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html)..  
Backend:
[Django](https://docs.djangoproject.com/en/2.1/),
[PostgreSQL](https://www.postgresql.org/),
[Django-Rest-Framework](http://www.django-rest-framework.org/tutorial/quickstart/),
[djangorestframework-recursive](https://github.com/heywbj/django-rest-framework-recursive),
[django-rest-framework-jwt](https://github.com/GetBlimp/django-rest-framework-jwt)  
DevOps:
[Docker](https://www.docker.com/),
[Docker-Compose](https://docs.docker.com/compose/),
[pgAdmin](https://www.pgadmin.org/docs/pgadmin4/3.x/),
[Dafny](https://rise4fun.com/Dafny/tutorial),
[Django-test](https://docs.djangoproject.com/en/2.1/topics/testing/overview/)

## Getting involve

### Set Your Working Branch

```bash
# create to your branch and working there
$ git checkout -b YOUR_BRANCH_NAME

# when you finshish, push the commits
$ git add && git commmit && git push
# IF you are push this branch FIRST TIME, you may use this line
$ git push --set-upstream origin YOUR_BRANCH_NAME
```

## Docker Environment

First, we need to install: 
[Docker Community Edition](https://docs.docker.com/install/#releases)
and
[Docker Compose](https://docs.docker.com/compose/install/#install-compose)  

That's all we need. Then you can type:

```bash
# startup the app, use (Ctrl +C) to exit
$ sudo docker-compose up 
```

Or, you don't want that much information, you can:

```bash
# Filter out the message of specified service
$ sudo docker-compose up | egrep "frontend"

# Or: detach the message when you up the app 
$ sudo docker-compose up -t
# Get the logged messages
$ sudo docker-compose logs
# Shutdown the app
$ sudo docker-compose down
```

There's a way to attach to the running container, use (Ctrl + D) to exit.

```bash
# attach backend
$ ./attach.sh backend
# run create a super user for management
# The id may not be same
root@6da3612aff4c:/usr/src/app# ./manage.py createsuperuser

# attach to frontend
$ ./attach.sh frontend
# add more dependencies
root@8a47db617648:/app# npm i -S @vue/ui
```

## APIs Documents

The api document is in [api.http](./api.http); You need to run it via [vscode Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

You can install it via this command in vscode command panel (Ctrl + Shift + P):

```bash
ext install humao.rest-client
```

## URLs

URL | Detail
:--- | :---
http://localhost:8000/ | Index of party whip's  
http://localhost:8080/ | Home Page (Backend)
http://localhost:8000/admin | Django admin
http://localhost:8081/ | pgAdmin: GUI of PostgreSQL 

## Some Helpful Commands (Deprecated)

```bash
# build for production with minification
$ yarn build

# build for production and view the bundle analyzer report
$ yarn build --report

# <!-- These two can not run, doesn't matter -->
# run unit tests
$ npm run unit

# run all tests
$ npm test
```
