import boto3
import os

client = boto3.client('ec2')
regions = client.describe_regions()

for region in regions['Regions']:
    print('** '+region['RegionName']+' **')
    os.system('docker build -t getpublicip .')
    os.system('aws ecr get-login-password --region '+region['RegionName']+' --profile Extensions | docker login --username AWS --password-stdin 070176467818.dkr.ecr.'+region['RegionName']+'.amazonaws.com')
    os.system('docker tag getpublicip:latest 070176467818.dkr.ecr.'+region['RegionName']+'.amazonaws.com/getpublicip:latest')
    os.system('docker push 070176467818.dkr.ecr.'+region['RegionName']+'.amazonaws.com/getpublicip:latest')
