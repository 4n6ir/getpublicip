import os

regions = []
regions.append('us-east-1')
regions.append('us-east-2')
regions.append('us-west-2')

for region in regions:
    print('** '+region+' **')
    os.system('docker build -t getpublicip .')
    os.system('aws ecr get-login-password --region '+region+' --profile Extensions | docker login --username AWS --password-stdin 070176467818.dkr.ecr.'+region+'.amazonaws.com')
    os.system('docker tag getpublicip:latest 070176467818.dkr.ecr.'+region+'.amazonaws.com/getpublicip:latest')
    os.system('docker push 070176467818.dkr.ecr.'+region+'.amazonaws.com/getpublicip:latest')
