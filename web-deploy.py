#!/usr/bin/env python3
"""
Simplest script:
Downloads two files from GitHub (raw versions) and uploads them to an S3 bucket,
then enables public static website hosting.
"""

import boto3
import botocore
import requests
import json
import mimetypes

# ---- Configuration ----
REGION = "us-east-2"
BUCKET_NAME = "python-2522-public-bucket"   # must be globally unique

INDEX_URL = "https://raw.githubusercontent.com/ravi2krishna/login-2514/main/index.html"
IMG_URL = "https://raw.githubusercontent.com/ravi2krishna/login-2514/main/img_avatar2.png"
INDEX_FILE = "index.html"
IMG_FILE = "img_avatar2.png"
# ------------------------
    
# 1️⃣ Download files directly
print("📥 Downloading files...")
index_data = requests.get(INDEX_URL)
img_data = requests.get(IMG_URL)
print("✅ Files downloaded.")

with open(IMG_FILE, 'wb') as file:
        for chunk in img_data.iter_content():
            file.write(chunk)
print(f"✅ File '{IMG_FILE}' downloaded successfully.")


with open(INDEX_FILE, 'wb') as file:
        for chunk in index_data.iter_content():
            file.write(chunk)
print(f"✅ File '{INDEX_FILE}' downloaded successfully.")

# 2️⃣ Create public S3 bucket
s3 = boto3.client("s3")
try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={"LocationConstraint": REGION}
    )
    print(f"✅ Created public bucket: {BUCKET_NAME}")
except Exception as e:
    print("Error creating bucket:", e)

# Try to allow public access via bucket policy (preferred over ACL)
policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "PublicReadGetObject",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*"
    }]
}

try:
    # Attempt to disable public block for this bucket (may be denied by account settings)
    try:
        s3.put_public_access_block(
            Bucket=BUCKET_NAME,
            PublicAccessBlockConfiguration={
                "BlockPublicAcls": False,
                "IgnorePublicAcls": False,
                "BlockPublicPolicy": False,
                "RestrictPublicBuckets": False,
            }
        )
        print("ℹ️ Attempted to modify PublicAccessBlock for the bucket.")
    except botocore.exceptions.ClientError as ex:
        print("ℹ️ Could not modify PublicAccessBlock (may be account-enforced):", ex.response.get("Error", {}).get("Message"))

    s3.put_bucket_policy(Bucket=BUCKET_NAME, Policy=json.dumps(policy))
    print("✅ Bucket policy applied to allow public GET on objects.")
except botocore.exceptions.ClientError as e:
    print("⚠️ Could not apply bucket policy:", e.response.get("Error", {}).get("Message"))


# 3️⃣ Enable static website hosting (index.html)
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_website.html
s3.put_bucket_website(
    Bucket=BUCKET_NAME,
    WebsiteConfiguration={"IndexDocument": {"Suffix": "index.html"}}
)
print("🌐 Static website hosting enabled.")

# 4️⃣ Upload the two files
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_object.html
print("📤 Uploading files...")
# s3.put_object(Bucket=BUCKET_NAME, Key="index.html")
# s3.put_object(Bucket=BUCKET_NAME, Key="img_avatar2.png")


# ... later, when uploading ...
print("📤 Uploading files...")
for local_name in (INDEX_FILE, IMG_FILE):
    content_type = mimetypes.guess_type(local_name)[0] or "application/octet-stream"
    s3.upload_file(local_name, BUCKET_NAME, local_name, ExtraArgs={"ContentType": content_type})
print("✅ Files uploaded successfully!")

# 5️⃣ Print the live website endpoint
endpoint = f"http://{BUCKET_NAME}.s3-website-{REGION}.amazonaws.com"
print("\n🌎 Your website is live at:")
print(endpoint)
print("\n(Open in browser — may take ~1 minute to propagate.)")
