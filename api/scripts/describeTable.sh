#!/usr/bin/env bash

aws dynamodb describe-table \
  --endpoint-url http://localhost:8000 \
  --table-name $1
