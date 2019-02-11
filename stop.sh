#!/bin/bash
# This only works from console, kept open, that `start.sh` was called from

RUNSERVER=$(ps|grep runserver|head -1|cut -d' ' -f1)
kill $RUNSERVER
RUNSERVER=$(ps|grep runserver|head -1|cut -d' ' -f1)
kill $RUNSERVER

DYNAMO=$(ps|grep startDynamo.sh|cut -d' ' -f1)
kill $DYNAMO

# DYNAMO=$(ps|grep DynamoDBLocal.jar|cut -d' ' -f1)
# kill $DYNAMO
# DYNAMO=$(ps|grep dynamodb-local|cut -d' ' -f1)
# kill $DYNAMO
