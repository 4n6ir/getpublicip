#!/usr/bin/env python3
import boto3
import os

import aws_cdk as cdk

from getpublicip.getpublicip_stack import GetpublicipStack

app = cdk.App()

client = boto3.client('ec2')
regions = client.describe_regions()

for region in regions['Regions']:

    #command = 'aws ecr get-login-password --region '+region['RegionName']+' --profile Extensions | docker login --username AWS --password-stdin 070176467818.dkr.ecr.'+region['RegionName']+'.amazonaws.com'
    #os.system(command)

    GetpublicipStack(
        app, 'GetpublicipStack-'+region['RegionName'],
        env = cdk.Environment(
            account = os.getenv('CDK_DEFAULT_ACCOUNT'),
            region = region['RegionName']
        ),
        synthesizer = cdk.DefaultStackSynthesizer(
            qualifier = '4n6ir'
        )
    )

cdk.Tags.of(app).add('Alias','Extensions')
cdk.Tags.of(app).add('GitHub','https://github.com/4n6ir/getpublicip.git')

app.synth()