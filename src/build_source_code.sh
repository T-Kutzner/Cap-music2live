#!/bin/bash
mkdir ../infrastructure/build

cd fetch_albums_lambda
zip -r ../../infrastructure/build/fetch_albums_lambda.zip .