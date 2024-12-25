import boto3

# Create an S3 client
client = boto3.client('s3', region_name='ap-south-1')  # Replace 'your-region' with your desired AWS region, e.g., 'us-west-2'

# Create the S3 bucket
response = client.create_bucket(
    Bucket='newpb3bkt',  # Replace 'your-bucket-name' with your desired bucket name
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'  # Replace 'your-region' with the same region as above, e.g., 'us-west-2'
    }
)

print(f"Bucket {response['Location']} created successfully!")

