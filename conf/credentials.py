"""
This config file would have the credentials
[default]
aws_access_key_id = "enter aws id"
aws_secret_access_key = "enter aws secret access key"

###
one can find these keys in aws profile in right upper conrner of aws console
  ->https://console.aws.amazon.com/iam/home#/security_credentials
  ->Access keys (access key ID and secret access key)
  
or just visit aws credentials in your home directory (for linux or mac)
  cd ~./aws
  gedit credentials
  gedit config
"""

#aws
aws_access_key_id= 'enter aws id'
aws_secret_access_key='enter aws secret access key'
region='ap-south-1'

#lambda function name
lambda_function_name = 'patient_health_record'
