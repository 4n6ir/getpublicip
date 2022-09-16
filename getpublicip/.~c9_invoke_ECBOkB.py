from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_lambda as _lambda,
)

from constructs import Construct

class GetpublicipStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)




