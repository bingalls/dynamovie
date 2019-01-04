#!/bin/bash

aws dynamodb scan --endpoint-url http://localhost:8000 --table-name Movies
