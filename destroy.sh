#!/bin/bash
cd ./infrastructure
terraform destroy -var-file="spotify_api_keys.tfvars" -auto-approve