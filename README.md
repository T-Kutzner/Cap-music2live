# Capstone Project AWS
## Title: music2live
Fetch album data from a music API of an artist of interest and save the data in a database.
Check the API once a day and when a new album releases, get a notification via mail.

### used
- AWS: S3, Lambda function, DynamoDB, CloudWatch, VPC, EC2
- deploy with Terraform, code with Python3 (boto3 SDK), API Spotify
- versioning: Git, GitHub