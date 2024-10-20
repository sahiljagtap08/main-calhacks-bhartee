import boto3
import os

s3 = boto3.client('s3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

BUCKET_NAME = 'bharteeai-interview-recordings'

def upload_file(file_name, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, BUCKET_NAME, object_name)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    return True

def download_file(object_name, file_name):
    try:
        s3.download_file(BUCKET_NAME, object_name, file_name)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    return True

def delete_file(object_name):
    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=object_name)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    return True