resource "aws_s3_bucket" "terraform-example" {
  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}