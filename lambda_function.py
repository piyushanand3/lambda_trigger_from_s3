import boto3
import logging
import urllib.parse

# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Lambda function triggered.")

    # Retrieve the bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    logger.info(f"Bucket: {bucket}, Key: {key}")

    # Extract the folder name from the object key and decode it
    folder = key.split('/')[3]
    folder = urllib.parse.unquote(folder)
    logger.info(f"Folder: {folder}")

    # Extract the object name from the key and decode it
    object_name = key.split('/')[-1]
    object_name = urllib.parse.unquote(object_name)
    logger.info(f"Object name: {object_name}")

    # Check if the folder name starts with "folder=" and if the object name is "_demo"
    if not (folder.startswith('host_id=') and object_name == "_demo"):
        return  # Ignore Lambda execution

    # Perform your desired actions here
    logger.info("Hello, World!")

    # Add your code logic here to process
