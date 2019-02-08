# Dynamovie
Single Page Web App to manage a movie database using AWS DynamoDB

## Install
### Requirements
Currently only configured for local development, with
* node v11.6.0
* python 3.7.2
* vue 3.2.3

Npm's `dynalite` package claims easy local DynamoDB, but is not available for the
current Node version.

### Linux
* todo

### Mac OSX
* Install [Homebrew](https://brew.sh/)
* `brew install python3 --with-brewed-openssl`
* `brew install awscli cask node pyenv-virtualenv pyenv-virtualenvwrapper`
* `brew cask install dynamodb-local`
Dynamovie: A responsive, single page progressive movie database using Amazon's DynamoDB.
It is possible to adapt this with your legacy web application.
Uses Quasar Vue.js framework, and Python Django ReST framework.

### MS Windows
* todo
* Consider Cygwin or Windows 10 Bash shell

### All
Linux may require `sudo` for the following
* `npm i -g eslint-plugin-vue quasar-cli vue-cli @vue/cli-init`
* `git clone git@github.com:bingalls/dynamovie.git`
* `cd dynamovie`

### DynyamoDB Local Setup
* `cd api/scripts`
* `bash createMoviesTable.sh`
* `bash seedMovie.sh` # optional

### Python Setup
* `cd api`
* `python3 -m virtualenv venv`
* `pip3 check`
* `pip3 install -r requirements.txt`

Mac & Linux users may clean up newlines for git:
* `find venv -name RECORD|xargs dos2unix -`

## Run
### Dynamodb Local
* `bash api/scripts/startDynamo.sh`

### Python ReST API Server
* `cd dynamovie/`
* `source venv/bin/activate`
* `cd dynamovie/api`
* `python3 manage.py runserver`

### Vue.js Web Server
* `cd dynamovie/web/`
* `quasar dev`

## Road Map
This is development code, not yet ready for production. With community support, the following
will be improved:

* Font in select is too big
* delete & update loses filter of data
* Quasar is still a beta release
* As few files have been changed, to make upgrade easier. For example, side menu is unchanged.
* CORS is configured to allow all hosts
* No TLS, nor authentication. Important for updates & deletes
* API's localhost setting in Index.vue should be moved to quasar.conf.js
* No tests have been written. Only tested with local DynamoDB
* API can be richer: versioning, schema, graphql, etc
* Pagination is currently client side, only. Server pagination is commented.
* Studios & Genres come from a limited static list
* Move to TypeScript, just like the next version 
* The table is too wide for mobile. Currently, no feasible solution
