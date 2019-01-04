#!/usr/bin/env bash

#aws dynamodb create-table \
#  --endpoint-url http://localhost:8000 \
#  --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
#  --table-name movies \
#  --key-schema AttributeName=movie_id,KeyType=HASH \
#    AttributeName=genre,KeyType=S \
#  --attribute-definitions AttributeName=movie_id,AttributeType=S \
#    AttributeName=genre,AttributeType=S \

aws dynamodb create-table --endpoint-url http://localhost:8000 \
--table-name Movies \
--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
--attribute-definitions AttributeName=Title,AttributeType=S \
  AttributeName=Genre,AttributeType=S \
  AttributeName=Studio,AttributeType=S \
--key-schema AttributeName=Title,KeyType=HASH \
  AttributeName=Genre,KeyType=RANGE \
  AttributeName=Studio,KeyType=RANGE \
