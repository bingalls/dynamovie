#!/usr/bin/env bash

aws dynamodb delete-item --endpoint-url http://localhost:8000 \
--table-name Movies \
--key "{\"Title\": {\"S\": \"${1}\"}}"
