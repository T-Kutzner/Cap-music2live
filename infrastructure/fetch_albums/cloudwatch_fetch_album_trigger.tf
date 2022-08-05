resource "aws_cloudwatch_event_rule" "every_day" {
    name = "every-day"
    description = "Fires every day"
    schedule_expression = "rate(1 day)"
}

resource "aws_cloudwatch_event_target" "fetch_albums_event" {
    rule = aws_cloudwatch_event_rule.every_day.name
    target_id = "fetch_albums_event"
    arn = aws_lambda_function.fetch_albums_lambda.arn
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_fetch_albums_lambda" {
    statement_id = "AllowExecutionFromCloudWatch"
    action = "lambda:InvokeFunction"
    function_name = aws_lambda_function.fetch_albums_lambda.function_name
    principal = "events.amazonaws.com"
    source_arn = aws_cloudwatch_event_rule.every_day.arn
}