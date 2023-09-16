import os

os.system('aws ecr-public get-login-password --region us-east-1 --profile Extensions | docker login --username AWS --password-stdin public.ecr.aws/forensicir')
os.system('docker build -t getpublicip .')
os.system('docker tag getpublicip:latest public.ecr.aws/forensicir/getpublicip:latest')
os.system('docker push public.ecr.aws/forensicir/getpublicip:latest')
