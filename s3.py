import boto3
import pandas as pd
import datetime
import time
import matplotlib
import matplotlib.pyplot as plt

d = datetime.datetime.now()
Current_Date= "{}{}{}".format(d.month, d.day, d.year)
#Check if user is already login or not
session=boto3.Session()
if session is None:
	try:
		print('Enter the Details to start whitebox testing')
		ACCESS_KEY=input('Enter the Access key : ')
		SECRET_KEY=input('Enter the Secret key : ')
		SESSION_TOKEN=input('Enter the Session token : ')
		client = boto3.client('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,aws_session_token=SESSION_TOKEN)
	except Exception:
			raise CustomException(e.message,'worong input')
	else:	
		print('Echo Do you want to further for testing with same account')
		user=input('Enter the option yes or no : ')
		if user == 'yes' or user=='y':
			time.sleep(5)
			client = boto3.client('s3')
			response = client.list_buckets()
			print(response)
		else :
			print('Enter the new user credential for performing the output')
			ACCESS_KEY=input('Enter the Access key : ')
			SECRET_KEY=input('Enter the Secret key : ')
			SESSION_TOKEN=input('Enter the Session token : ')
			client = boto3.client('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,aws_session_token=SESSION_TOKEN)
			client = boto3.client('s3')
			repsone=client.list_buckets()
			print(response)
        	print('Process Sucessfull')

