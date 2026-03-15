import boto3
import os 
from dotenv import load_dotenv
load_dotenv()
class AWS:
  def __init__(self):
    self.s3 = self.Connect_to_s3()

  def Connect_to_s3(self):
    s3_client = boto3.client(
        's3',
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name = os.getenv('AWS_REGION','ap-south-1')
    )
    return s3_client
   
  def Upload_to_s3(self,bucket_name,s3_file_name,local_file):
    
    self.s3.upload_file(local_file,bucket_name,s3_file_name)
    print(f'the {bucket_name} has got stored {local_file} as the {s3_file_name}')

  def download_to_s3(self,bucket_name,s3_file_name,local_file):
    
    self.s3.download_file(bucket_name,s3_file_name,local_file)
    print(f'the {bucket_name} has got recived {local_file} as the {s3_file_name}')


  def Create_s3_bucket(self,bucket_name:str):
    region = os.getenv('AWS_REGION','ap-south-1')
    try:
      self.s3.create_bucket(
        Bucket = bucket_name,
        CreateBucketConfiguration = {
          'LocationConstraint':region
        }
      )
      print(f'the bucket {bucket_name} has been created')
    except Exception as e:
      print(f'there is an error {e}')      
