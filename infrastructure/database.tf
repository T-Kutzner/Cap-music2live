resource "aws_dynamodb_table" "albums" {
  name           = "albums"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "artist"

  attribute {
    name = "artist"
    type = "S"
  }
}