provider "aws" {
  region = "us-west-1"
}

resource "aws_iam_role" "application_lambda_role" {
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": [
          "lambda.amazonaws.com"
        ]
      },
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_s3_bucket" "lambdas_bucket" {}

resource "aws_s3_bucket_object" "lambda_package" {
  bucket = aws_s3_bucket.lambdas_bucket.id
  key    = filemd5(var.lambda_function_name)
  source = var.lambda_function_name

  # The filemd5() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the md5() function and the file() function:
  # etag = "${md5(file("path/to/file"))}"
  etag = filemd5(var.lambda_function_name)
}

resource "aws_lambda_function" "application_lambda" {
  runtime = "python3.8"
  s3_bucket = aws_s3_bucket.lambdas_bucket.id
  s3_key = aws_s3_bucket_object.lambda_package.id
  function_name = "uniwersytet-sla-by-terraform-production"
  role = aws_iam_role.application_lambda_role.arn
  handler = "handler.lambda_handler"
  publish = false
  source_code_hash = filebase64sha256(var.lambda_function_name)
  timeout = 60
  memory_size = 512

  environment {
    variables = {
      ALA = var.dummy_var
    }
  }
}