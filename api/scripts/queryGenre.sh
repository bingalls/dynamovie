#!/usr/bin/env bash

aws dynamodb query --endpoint-url http://localhost:8000 --table-name Movies \
--key-condition-expression "Genre = :genre" \
--expression-attribute-values '{":genre": {"S": "Science Fiction"}}'
