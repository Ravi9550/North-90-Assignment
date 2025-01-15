import json
import boto3
from base64 import b64decode
from botocore.exceptions import NoCredentialsError

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event['bucket_name']
    file_name = event['file_name']
    file_content_base64 = event['file_content']  
    
    try:
        file_content = b64decode(file_content_base64)
        
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content,
            ContentType='application/pdf'  
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"File {file_name} uploaded successfully to {bucket_name}.")
        }
        
    except NoCredentialsError:
        return {
            'statusCode': 403,
            'body': json.dumps("Access denied: No AWS credentials found.")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error occurred: {str(e)}")
        }
