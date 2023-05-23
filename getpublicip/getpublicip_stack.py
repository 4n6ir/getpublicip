import cdk_nag

from aws_cdk import (
    Aspects,
    RemovalPolicy,
    Stack,
    aws_lambda as _lambda
)

from constructs import Construct

class GetpublicipStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        Aspects.of(self).add(
            cdk_nag.AwsSolutionsChecks()
        )

        Aspects.of(self).add(
            cdk_nag.HIPAASecurityChecks()    
        )

        Aspects.of(self).add(
            cdk_nag.NIST80053R5Checks()
        )

        Aspects.of(self).add(
            cdk_nag.PCIDSS321Checks()
        )

        cdk_nag.NagSuppressions.add_stack_suppressions(
            self, suppressions = [
            ]
        )

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
                description = 'AWS Lambda Extension captures the Public IP into Cloud Watch logs at execution using Requests v2.31.0 Python library.',
                layer_version_name = 'getpublicip',
                license = 'Apache-2.0 License',
                removal_policy = RemovalPolicy.DESTROY
            )

        elif region == 'eu-central-2' or region == 'eu-south-2' or region == 'ap-south-2' or region == 'ap-southeast-4':

            layer = _lambda.LayerVersion(
                self, 'layer',
                code = _lambda.Code.from_asset('bundle/extension.zip'),
                compatible_runtimes = [
                    _lambda.Runtime.PYTHON_3_7,
                    _lambda.Runtime.PYTHON_3_8,
                    _lambda.Runtime.PYTHON_3_9,
                    _lambda.Runtime.PYTHON_3_10
                ],
                description = 'AWS Lambda Extension captures the Public IP into Cloud Watch logs at execution using Requests v2.31.0 Python library.',
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
                    _lambda.Runtime.PYTHON_3_9,
                    _lambda.Runtime.PYTHON_3_10
                ],
                description = 'AWS Lambda Extension captures the Public IP into Cloud Watch logs at execution using Requests v2.31.0 Python library.',
                layer_version_name = 'getpublicip',
                license = 'Apache-2.0 License',
                removal_policy = RemovalPolicy.DESTROY
            )

        layer.add_permission(
            id = 'permission',
            account_id = '*'
        )
