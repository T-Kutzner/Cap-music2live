resource "aws_dynamodb_table" "albums" {
  name           = "albums"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "artist_id"
  range_key      = "album_id"

  attribute {
    name = "artist_id"
    type = "S"
  }

  attribute {
    name = "album_id"
    type = "S"
  }
}