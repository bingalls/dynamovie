#!/usr/bin/env bash

aws dynamodb put-item --endpoint-url http://localhost:8008 \
--table-name Movies \
--item "{\"Title\": {\"S\": \"Star Wars IX\"}, \
  \"Genre\":{\"S\": \"Science Fiction\"}, \
  \"Studio\":{\"S\": \"Lucas Films\"}, \
  \"Director\":{\"S\": \"JJ Abrams\"}, \
  \"Actor\":{\"SS\": [\"Domhnall Gleeson\", \"Daisy Ridley\", \"Adam Driver\"]} }"

aws dynamodb put-item --endpoint-url http://localhost:8008 \
--table-name Movies \
--item "{\"Title\": {\"S\": \"Star Trek: Into Darkness\"}, \
  \"Genre\":{\"S\": \"Science Fiction\"}, \
  \"Studio\":{\"S\": \"Disney\"}, \
  \"Director\":{\"S\": \"JJ Abrams\"}, \
  \"Actor\":{\"SS\": [\"Chris Pine\", \"Zachary Quinto\", \"Zoe Saldana\"]} }"
