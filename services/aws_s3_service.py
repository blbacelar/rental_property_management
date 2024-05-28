import os

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

S3_BUCKET = os.getenv('S3_BUCKET')
S3_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
S3_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
S3_REGION = os.getenv('AWS_REGION')

s3 = boto3.client(
    's3',
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    region_name=S3_REGION
)

def upload_file_to_s3(file, bucket_name, acl="public-read"):
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
        return f"https://{bucket_name}.s3.{S3_REGION}.amazonaws.com/{file.filename}"
    except NoCredentialsError:
        return "Credentials not available"
    except PartialCredentialsError:
        return "Incomplete credentials provided"
