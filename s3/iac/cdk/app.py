#!/usr/bin/env python3

from aws_cdk import core
from my_cdk_app.my_s3_bucket_stack import MyS3BucketStack

app = core.App()
MyS3BucketStack(app, "MyS3BucketStack")

app.synth()
