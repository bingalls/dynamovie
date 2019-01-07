#!/usr/bin/env bash

# Compact syntax https://docs.aws.amazon.com/cli/latest/reference/dynamodb/index.html
aws dynamodb create-table --endpoint-url http://localhost:8000 \
--table-name Movies \
--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
--attribute-definitions AttributeName=Title,AttributeType=S \
--key-schema AttributeName=Title,KeyType=HASH \


#  AttributeName=Genre,AttributeType=S \
#  AttributeName=Genre,KeyType=RANGE \
