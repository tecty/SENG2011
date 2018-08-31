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

```bash
# in Ubuntu
sudo apt install python3 python3-venv virtualenv
```


```bash
# Create Virtual environment if you haven't
$ virtualenv venv -p `which python3` 
```

```bash
# activate the virtual envirnoment
$ source venv/bin/activate
```

### Install dependencies and setup the database

```bash
# install python dependencies 
(venv) $ pip install -r requirements.txt

# setup the database
(venv) $ ./init_db.sh
```

### Run the Server

A shell to run django's httpd.

```bash
# Run in local
(venv) $ ./manage.py runserver

# ALTERNATIVE: start the server to public
(venv) $ sudo python manage.py runserver 0:80
```

# Frontend

## Install the System Environment

Install node.js: [Node Install Use Package Manager](https://nodejs.org/en/download/package-manager/)  

Install yarn: [Yarn Install Documents](https://yarnpkg.com/zh-Hans/docs/install#debian-stable)

## Install The Dependencies of Frontend

``` bash
# install dependencies
$ yarn install
```

## Run the Frontend

You also need another shell to keep fronend server running.

```bash
# serve with hot reload at localhost:8080
$ yarn dev
```

## Some Helpful Commands

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

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).  
Also you may want to checkout
[vue](https://cn.vuejs.org/v2/guide/),
[vuex](https://vuex.vuejs.org/guide/),
[Vuetify](https://vuetifyjs.com/en/getting-started/quick-start),
[Vue-router](https://router.vuejs.org/),
[Axios](https://cn.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html)..

## URLs

### Frondend

URL | Detail
:--- | :---
http://127.0.0.1:8080/#/ | Home Page
http://localhost:8080/#/post | Post Tasks Page

### Backend

URL | Detail
:--- | :---
http://127.0.0.1:8000/admin | Django admin
http://127.0.0.1:8000/api-v0/ | Index of party whip's api  
http://127.0.0.1:8000/ | Index of party whip's  
