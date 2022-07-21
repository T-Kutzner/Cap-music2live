#!/bin/bash
TERRAFORM_S3_BUCKET_NAME=mysongartistalbumtkbucket
bucket_not_exists=$(aws s3api head-bucket --bucket $TERRAFORM_S3_BUCKET_NAME 2>/dev/null && echo false || echo true)
if $bucket_not_exists
then
    aws s3api create-bucket --bucket $TERRAFORM_S3_BUCKET_NAME --region eu-central-1 --create-bucket-configuration LocationConstraint=eu-central-1
else
    echo "terraform bucket already exists"
fi