#!/usr/bin/env bash

aws dynamodb describe-table \
  --endpoint-url http://localhost:8008 \
  --table-name $1
