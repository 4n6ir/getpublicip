#!/usr/bin/env python3
import os

import aws_cdk as cdk

from getpublicip.getpublicip_stack import GetpublicipStack

app = cdk.App()

GetpublicipStack(
    app, 'GetpublicipStack-us-east-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

GetpublicipStack(
    app, 'GetpublicipStack-us-east-2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

GetpublicipStack(
    app, 'GetpublicipStack-us-west-2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-west-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

cdk.Tags.of(app).add('Alias','Extensions')
cdk.Tags.of(app).add('GitHub','https://github.com/4n6ir/getpublicip.git')

app.synth()