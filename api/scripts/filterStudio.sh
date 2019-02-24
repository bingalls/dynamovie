#!/usr/bin/env bash

aws dynamodb scan --endpoint-url http://localhost:8008 --table-name Movies \
--filter-expression "Studio = :studio" \
--expression-attribute-values '{":studio":{"S":"Walt Disney"}}'
