import boto3

# Initialize the S3 client
client = boto3.client('s3', region_name='ap-south-1')  # Replace 'your-region' with the region where the bucket is located

# Specify the bucket name
bucket_name = 'newpb3bkt'  # Your actual bucket name

# Delete the bucket
def delete_empty_bucket(bucket_name):
    try:
        # Delete the bucket
        client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully!")
    except Exception as e:
        print(f"Error deleting bucket: {e}")

# Call the function to delete the bucket
delete_empty_bucket(bucket_name)

