#!/bin/bash
cd ./src
sh build_source_code.sh
cd ..
cd ./infrastructure
sh setup_terraform_state_s3_bucket.sh
terraform init
terraform apply -var-file="spotify_api_keys.tfvars" -auto-approve