resource "aws_lambda_function" "fetch_albums_lambda" {

  filename      = "build/fetch_albums_lambda.zip"
  function_name = "fetch_albums_lambda"
  role          = var.role_arn
  handler       = "fetch_album.handler"

  source_code_hash = filebase64sha256("build/fetch_albums_lambda.zip")

  runtime = "python3.9"
  timeout = 600
  layers = [aws_lambda_layer_version.requests_layer.arn]

  environment {
    variables = {
      ALBUM_TABLE_NAME = var.album_table_name
      API_CLIENT_ID = var.api_client_id
      API_CLIENT_SECRET = var.api_client_secret
    }
  }
}