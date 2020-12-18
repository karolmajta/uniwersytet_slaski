terraform {
  backend "s3" {
    bucket = "uniwersytet-slaski-tfstate"
    region = "us-west-1"
    key = "uniwersytet_slaski/production/terraform.tfstate"
    dynamodb_table = "uniwersytet-slaski-terraform-locks"
  }
}