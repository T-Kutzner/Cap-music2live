module "fetch_albums" {
    source = "./fetch_albums"

    album_table_name = aws_dynamodb_table.albums.name
    role_arn = local.role_arn
    api_client_id = var.api_client_id
    api_client_secret = var.api_client_secret
}