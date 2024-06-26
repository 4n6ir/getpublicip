# getpublicip

The Lambda Extension allows you to attach an existing Function to run in the same execution environment by sharing CPU, Memory, Disk Storage, Environment Variables, and IAM Permissions. Lambda supports up to 10 extensions (multiple per layer) and up to 5 layers per function, counting against the unzipped deployment package size limit of 250 MB. It adds benefits but introduces potential threats that justify defining an SCP to mitigate the risk.

##### Potential Threats:

- Do you trust the external Lambda Extension or Lambda Layer attached to the Lambda Function not to inject malicious code?
- The extension could add code dependencies that may introduce vulnerabilities or provide a means for notorious activities.
- Lambda Layers do not show if they are publically shared or have access granted to external AWS Accounts in the console.

I have created Lambda Extention that captures the Public IP Address by visiting this AWS site to help reduce the request latency.

https://checkip.amazonaws.com

The Lambda Extension returns the following log entry in the Cloud Watch Logs. The account number is only available if the **AWS_ACCOUNT** environment variable is part of the Lambda deployment.

```json
{
    "publicip": "34.220.123.1",
    "timestamp": "09/08/2023 02:43:32.379936 UTC",
    "function": "AmazonblocksStack-gtfobin14961F10-bvnpSnvvSSfH",
    "region": "us-west-2",
    "account": "070176467818"
}
```

##### AWS Serverless Application Repository

https://serverlessrepo.aws.amazon.com

##### Cloud Development Kit (CDK) v2

```python
        region = Stack.of(self).region

        layer = _lambda.LayerVersion.from_layer_version_arn(
            self, 'layer',
            layer_version_arn = 'arn:aws:lambda:'+region+':070176467818:layer:getpublicip:12'
        )
```

##### Amazon ECR Public Gallery

```
public.ecr.aws/forensicir/getpublicip:latest
```

https://gallery.ecr.aws/forensicir/getpublicip

##### Lambda Container Extension

```dockerfile
### 2.136.0 (build 94fd33b) ###
FROM 070176467818.dkr.ecr.us-west-2.amazonaws.com/getpublicip:latest AS layer
FROM public.ecr.aws/lambda/python:latest
RUN yum -y update && yum clean all
### layer code ###
WORKDIR /opt
COPY --from=layer /opt/ .
### function code ###
WORKDIR /var/task
COPY gtfobin.py requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt --upgrade
CMD ["gtfobin.handler"]
```

##### Regions

- us-east-1
- us-east-2
- us-west-2
