#!/usr/bin/env python3

print("importing...")
import boto3
import sys
import os
print("starting...")

# Create an S3 client
s3 = boto3.client('s3')

# Get file name from command line argument
filename = 'files/' + sys.argv[1]
print(filename)
bucket_name = 'pigclass'
print("uploading...")

# Upload file to S3
s3.upload_file(filename, bucket_name, filename)
print("deleting file...")

# Remove file from Ubuntu server as it isn't needed anymore
os.remove(filename)
print("done.")
