from aws_cdk import (
    Stack,
    aws_s3 as s3,
    CfnOutput,
    RemovalPolicy
)
from constructs import Construct

class MyS3BucketStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket
        s3_bucket = s3.Bucket(
            self, 
            "MySampleBucket",
            versioned=True,  # Enable versioning
            removal_policy=RemovalPolicy.DESTROY,  # Automatically delete the bucket when the stack is destroyed
            auto_delete_objects=True,  # Automatically delete objects in the bucket when the bucket is destroyed
            public_read_access=False,  # Disable public read access
        )

        # Output the bucket name
        CfnOutput(
            self,
            "BucketNameOutput",
            value=s3_bucket.bucket_name,
            description="The name of the S3 bucket",
        )
