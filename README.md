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
