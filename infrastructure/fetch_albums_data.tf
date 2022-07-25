resource "aws_lambda_function" "fetch_albums_lambda" {
  # If the file is not in the current working directory you will need to include a 
  # path.module in the filename.
  filename      = "build/fetch_albums_lambda.zip"
  function_name = "fetch_albums_lambda"
  role          = "arn:aws:iam::959074398624:role/LabRole"
  handler       = "fetch_album.handler"

  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
  source_code_hash = filebase64sha256("build/fetch_albums_lambda.zip")

  runtime = "python3.9"
}