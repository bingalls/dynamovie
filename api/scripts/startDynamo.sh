#!/usr/bin/env bash

echo 'Running local dynamodb service. ^C to quit';
dynamodb-local --sharedDb;

echo 'Shutting down dynamodb';
