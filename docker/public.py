import os

os.system('aws ecr-public get-login-password --region us-east-1 --profile Extensions | docker login --username AWS --password-stdin public.ecr.aws/p4b7o4r9')
os.system('docker build -t getpublicip .')
os.system('docker tag getpublicip:latest public.ecr.aws/p4b7o4r9/getpublicip:latest')
os.system('docker push public.ecr.aws/p4b7o4r9/getpublicip:latest')
