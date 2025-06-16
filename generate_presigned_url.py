import boto3
from botocore.exceptions import ClientError
import sys

def generate_presigned_url(bucket_name, object_name, expiration=3600):
    s3 = boto3.client('s3')
    try:
        response = s3.generate_presigned_url('get_object',
                                            Params={'Bucket': bucket_name,
                                                    'Key': object_name},
                                            ExpiresIn=expiration)

    except ClientError as e:
        print(f" Error: {e}")
        return None
    
    return response


if __name__ == "__main__":
    bucket = "lam-975050050500-test-bucket"
    key = "test_file.txt"

    url = generate_presigned_url(bucket,key)
    if url:
        print(f" Presigned URL: \n{url}")