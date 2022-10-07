from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_lambda as _lambda
)

from constructs import Construct

class GetpublicipStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        region = Stack.of(self).region

        if region == 'me-central-1':

            layer = _lambda.LayerVersion(
                self, 'layer',
                code = _lambda.Code.from_asset('bundle/extension.zip'),
                compatible_runtimes = [
                    _lambda.Runtime.PYTHON_3_7,
                    _lambda.Runtime.PYTHON_3_8,
                    _lambda.Runtime.PYTHON_3_9
                ],
                description = 'AWS Lambda Extension captures the Public IP into Cloud Watch logs at execution using Requests v2.28.1 Python library.',
                layer_version_name = 'getpublicip',
                license = 'Apache-2.0 License',
                removal_policy = RemovalPolicy.DESTROY
            )

        else:

            layer = _lambda.LayerVersion(
                self, 'layer',
                code = _lambda.Code.from_asset('bundle/extension.zip'),
                compatible_architectures = [
                    _lambda.Architecture.ARM_64,
                    _lambda.Architecture.X86_64
                ],
                compatible_runtimes = [
                    _lambda.Runtime.PYTHON_3_7,
                    _lambda.Runtime.PYTHON_3_8,
                    _lambda.Runtime.PYTHON_3_9
                ],
                description = 'AWS Lambda Extension captures the Public IP into Cloud Watch logs at execution using Requests v2.28.1 Python library.',
                layer_version_name = 'getpublicip',
                license = 'Apache-2.0 License',
                removal_policy = RemovalPolicy.DESTROY
            )

        layer.add_permission(
            id = 'permission',
            account_id = '*'
        )
