#!/usr/bin/env bash

# Compact syntax https://docs.aws.amazon.com/cli/latest/reference/dynamodb/index.html
aws dynamodb create-table --endpoint-url http://localhost:8000 \
--table-name Movies \
--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
--attribute-definitions AttributeName=Title,AttributeType=S \
  AttributeName=Genre,AttributeType=S \
--key-schema AttributeName=Title,KeyType=HASH \
  AttributeName=Genre,KeyType=RANGE \

#--local-secondary-indexes IndexName=Studio,\
#KeySchema='[{AttributeName=Title,KeyType=S},{AttributeName=Studio,KeyType=S}]',\
#Projection='{ProjectionType=ALL}'\

# Projection='{ProjectionType=INCLUDE,NonKeyAttributes=[S,S]}'\
# Projection='{ProjectionType=KEYS_ONLY}'\
