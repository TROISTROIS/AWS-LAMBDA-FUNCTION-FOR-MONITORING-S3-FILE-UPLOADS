import boto3
import pandas as pd

def lambda_handler(event, context):
    # Get the S3 bucket and object key from the Lambda event trigger
    print("Event -------> ",event)
    print("Context *********", context)
    print("Records", event['Records'][0])
    bucket = event['Records'][0]['s3']['bucket']['name']
    print("S3 Bucket Name: ", bucket)
    file = event['Records'][0]['s3']['object']['key']
    print("File Name: ", file)
    size = event['Records'][0]['s3']['object']['size']
    print("File Size: ", size)

    size_thresh = 100 * (1024**2)
    if size <= size_thresh:
        return {
            'statusCode': 200,
            'body':{
                'Bucket Name': bucket,
                'S3 File Name': file,
                'S3 file size': size
            }
        }
    else:
        return {
            'statusCode':413,
            'body': "File Size Exceeds 100 MB. File size is {}".format(size)
        }



