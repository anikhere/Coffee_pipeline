import os 
from dotenv import load_dotenv
load_dotenv()
def Connect_to_s3():
    key = os.getenv("AWS_ACCESS_KEY_ID")
    secret = os.getenv("AWS_SECRET_ACCESS_KEY")
    print("KEY:", key)
    print("SECRET:", secret)
Connect_to_s3()

