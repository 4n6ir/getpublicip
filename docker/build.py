import boto3
import os

client = boto3.client('ec2')
regions = client.describe_regions()

for region in regions['Regions']:
    print('** '+region['RegionName']+' **')
    os.system('docker build -t latest .')
    os.system('aws ecr get-login-password --region '+region['RegionName']+' --profile Extensions | docker login --username AWS --password-stdin 070176467818.dkr.ecr.'+region['RegionName']+'.amazonaws.com')
    os.system('docker tag latest 070176467818.dkr.ecr.'+region['RegionName']+'.amazonaws.com/getpublicip')
    os.system('docker push 070176467818.dkr.ecr.'+region['RegionName']+'.amazonaws.com/getpublicip')
