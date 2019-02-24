#!/bin/bash

aws dynamodb scan --endpoint-url http://localhost:8008 --table-name Movies
