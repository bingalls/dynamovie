#!/bin/bash
# This only works from console, kept open, that `start.sh` was called from

RUNSERVER=$(ps|grep runserver|head -1|awk '{print $1}')
kill $RUNSERVER
RUNSERVER=$(ps|grep runserver|head -1|awk '{print $1}')
kill $RUNSERVER

DYNAMO=$(ps|grep startDynamo.sh|awk '{print $1}')
kill $DYNAMO

DYNAMO=$(ps|grep DynamoDBLocal.jar|awk '{print $1}')
kill $DYNAMO
DYNAMO=$(ps|grep dynamodb-local|awk '{print $1}')
kill $DYNAMO
