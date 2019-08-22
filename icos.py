"""
    Python code snippets to work with IBM Cloud Object Storage and the `ibm_boto3` library.
    ibm_boto3 can be installed using the command: `pip install ibm-cos-sdk`.
    Updated the last time at: 18:26 22/AUG/2019 by @vnderlev
"""

import json
import ibm_boto3
from ibm_botocore.client import Config


# Copy the ICOS credentials from the IBM Cloud Web page and save them as a json file named below. 
ICOS_JSONFILE = "icos_credentials.json"
with open(ICOS_JSONFILE) as json_file:
    icos_cred = json.load(json_file)
# An `ibm_boto3.client` object is stantiated with the provided credentials.
# The endpoint_url may be different depending on the region ICOS is instantiated.
icos = ibm_boto3.client(service_name="s3",
    ibm_api_key_id=icos_cred['apikey'],
    ibm_service_instance_id=icos_cred['resource_instance_id'],
    ibm_auth_endpoint="https://iam.cloud.ibm.com/identity/token",
    config=Config(signature_version="oauth"),
    endpoint_url="https://s3.us-south.cloud-object-storage.appdomain.cloud" # You can choose different endpoints.
    )

# list all the available buckets at this ICOS instance using `list_buckets()`.
for bucket in icos.list_buckets()['Buckets']:
    print(bucket['Name'])
# To create a bucket in ICOS use:
icos.create_bucket(Bucket='bucket_name')
# To delete a bucket in ICOS use:
icos.delete_bucket(Bucket='bucket_name')


def download_file_from_icos(icos_obj, bucket: str, local_file_name: str, key: str) -> None:
    """ 
        Function to download a file from a specific bucket at an ICOS instance.
        ARGS:
        @icos_obj -> an `ibm_boto3.client` object;
        @bucket -> a str with the bucket name;
        @local_file_name -> a str with the directory/name where the file will be saved; and
        @key -> a str with the name of the desired file inside the bucket.
    """
    try:
        icos_obj.download_file(Bucket=bucket, Key=key, Filename=local_file_name)
    except Exception as e:
        print(Exception, e)
    else:
        print('File `{}` downloaded from ICOS and saved locally as `{}`.'.format(key, local_file_name))


def upload_file_to_icos(icos_obj, bucket: str, local_file_name: str, key: str) -> None:
    """ 
        Function to download a file from a specific bucket at an ICOS instance.
        ARGS:
        @icos_obj -> an `ibm_boto3.client` object;
        @bucket -> a str with the bucket name;
        @local_file_name -> a str with the directory/name where the file to be uploaded is located; and
        @key -> a str with the name of the file that will be saved inside the bucket.
    """
    try:
        icos_obj.upload_file(Filename=local_file_name, Bucket=bucket, Key=key)
    except Exception as e:
        print(Exception, e)
    else:
        print('File `{}` uploaded to ICOS as `{}`.'.format(local_file_name, key))


# Define the desired bucket in the variable below.
BUCKET = ""
# Example usage:
download_file_from_icos(icos, BUCKET, "img2.zip", "img1.zip")
download_file_from_icos(icos, BUCKET, "img2.zip", "img1.zip")
