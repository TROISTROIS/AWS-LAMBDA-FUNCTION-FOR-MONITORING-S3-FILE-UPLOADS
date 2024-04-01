import boto3
import pandas as pd

def lambda_handler(event, context):
    # Get the S3 bucket and object key from the Lambda event trigger
    print(event)
