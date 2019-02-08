#!/bin/bash
./api/scripts/startDynamo.sh &
cd api
. ./venv/bin/activate
python3 manage.py runserver &
cd ../web
quasar dev
