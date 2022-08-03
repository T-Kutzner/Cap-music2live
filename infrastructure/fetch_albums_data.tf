resource "aws_lambda_function" "fetch_albums_lambda" {

  filename      = "build/fetch_albums_lambda.zip"
  function_name = "fetch_albums_lambda"
  role          = "arn:aws:iam::959074398624:role/LabRole"
  handler       = "fetch_album.handler"

  source_code_hash = filebase64sha256("build/fetch_albums_lambda.zip")

  runtime = "python3.9"

  layers = [aws_lambda_layer_version.requests_layer.arn]
}

resource "aws_lambda_layer_version" "requests_layer" {
  filename      = "build/requests_layer.zip"
  layer_name    = "requests_layer"

  compatible_runtimes = ["python3.9"]
}