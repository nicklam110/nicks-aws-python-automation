import boto3
import os

def upload_file(file_name, bucket_name, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f" Uploaded {file_name} to s3://{bucket_name}/{object_name}")
    except Exception as e:
        print(f" Upload failed: {e}")

if __name__ == "__main__":
    # Replace with your actual file and bucket name
    upload_file("test_file.txt", "lam-975050050500-test-bucket")
