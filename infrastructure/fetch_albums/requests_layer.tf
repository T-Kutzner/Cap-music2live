resource "aws_lambda_layer_version" "requests_layer" {
  filename      = "build/requests_layer.zip"
  layer_name    = "requests_layer"

  compatible_runtimes = ["python3.9"]
}