#!/usr/bin/env bash

aws dynamodb delete-table \
  --endpoint-url http://localhost:8000 \
  --table-name $1
