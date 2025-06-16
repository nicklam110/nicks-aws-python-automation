import boto3

def download_file(bucket_name, object_name, download_path):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, object_name, download_path)
        print(f" Downloaded {object_name} to {download_path}")
    except Exception as e:
        print(f" Download failed: {e}")

if __name__ == "__main__":
    download_file("lam-975050050500-test-bucket", "test_file.txt", "downloaded_test_file.txt")
