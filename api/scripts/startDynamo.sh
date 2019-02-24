#!/usr/bin/env bash

echo 'Running local dynamodb service. ^C to quit';
dynamodb-local --sharedDb -port 8008;

echo 'Shutting down dynamodb';
