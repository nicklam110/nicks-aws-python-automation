import boto3
import json

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]

def list_ec2_instances():
    ec2_data = []
    ec2 = boto3.client('ec2')
    regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]

    for region in regions:
        ec2_region = boto3.client('ec2', region_name=region)
        instances = ec2_region.describe_instances()
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                ec2_data.append({
                    'InstanceId': instance['InstanceId'],
                    'Region': region,
                    'State': instance['State']['Name'],
                    'Type': instance['InstanceType']
                })
    return ec2_data

def write_to_json(data, filename='aws_audit_output.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f" Results written to {filename}")

if __name__ == "__main__":
    print(" Auditing AWS resources...")
    audit_data = {
        's3_buckets': list_s3_buckets(),
        'ec2_instances': list_ec2_instances()
    }
    write_to_json(audit_data)
