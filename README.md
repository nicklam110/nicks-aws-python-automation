# AWS Python Automation

This repository contains simple AWS automation scripts using **Python** and **Boto3**, built as part of a cloud engineering upskilling project.

The scripts help interact with AWS services such as **S3** and **EC2** for tasks like listing resources, uploading/downloading files, and generating presigned URLs.

---

## Scripts

### `/s3_upload_download.py`
- Uploads a local file to a specified S3 bucket.
- Downloads a file from a specified S3 bucket to local storage.

### `/s3_presigned_url.py`
- Generates a presigned URL to securely access an S3 object.

### `/ec2_instance_list.py`
- Lists all EC2 instances in your AWS account (default region).

### `/resource_audit_tool.py`
- Combines EC2 + S3 listing into a single JSON output.
- Great for resource auditing and visibility (Week 2 project).

---

## How to Run

> All scripts assume that you have AWS CLI credentials already configured (via `aws configure`, SSO login, or environment variables).

1. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```powershell
    . .\venv\Scripts\activate

2. Install dependencies
   ```bash
   pip install -r requirements.txt

3. Run any script
   ```bash
   python s3_upload_download.py

