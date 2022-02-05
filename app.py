#!/usr/bin/env python3
import os

import aws_cdk as cdk

from remedy_lambda_public_ip_visibility.remedy_lambda_public_ip_visibility_stack import RemedyLambdaPublicIpVisibilityStack

app = cdk.App()

RemedyLambdaPublicIpVisibilityStack(
    app, 'RemedyLambdaPublicIpVisibilityStack',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = os.getenv('CDK_DEFAULT_REGION')
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

cdk.Tags.of(app).add('remedy-lambda-public-ip-visibility','remedy-lambda-public-ip-visibility')

app.synth()
