# getpublicip

The Lambda Extension allows you to attach an existing Function to run in the same execution environment by sharing CPU, Memory, Disk Storage, Environment Variables, and IAM Permissions. Lambda supports up to 10 extensions (multiple per layer) and up to 5 layers per function, counting against the unzipped deployment package size limit of 250 MB. It adds benefits but introduces potential threats that justify defining an SCP to mitigate the risk.

##### Potential Threats:

- Do you trust the external Lambda Extension or Lambda Layer attached to the Lambda Function not to inject malicious code?
- Lambda Layers do not show if they are publically shared or have access granted to external AWS Accounts in the console, making a potential route for limited data exfiltration.

I have created Lambda Extention that captures the Public IP Address by visiting this AWS site to help reduce the request latency.

https://checkip.amazonaws.com

The Lambda Extension returns the following log entry in the Cloud Watch Logs.

```
[get-public-ip] 3.216.79.240
```

##### Cloud Development Kit (CDK) v2

![awslambda](ICON.png)

```python
        region = Stack.of(self).region

        if region == 'ap-northeast-1' or region == 'ap-south-1' or region == 'ap-southeast-1' or \
            region == 'ap-southeast-2' or region == 'eu-central-1' or region == 'eu-west-1' or \
            region == 'eu-west-2' or region == 'me-central-1' or region == 'us-east-1' or \
            region == 'us-east-2' or region == 'us-west-2' or region == 'eu-central-2' or \
            region == 'eu-south-2' or region == 'ap-south-2': number = str(1)

        if region == 'af-south-1' or region == 'ap-east-1' or region == 'ap-northeast-2' or \
            region == 'ap-northeast-3' or region == 'ap-southeast-3' or region == 'ca-central-1' or \
            region == 'eu-north-1' or region == 'eu-south-1' or region == 'eu-west-3' or \
            region == 'me-south-1' or region == 'sa-east-1' or region == 'us-west-1': number = str(2)

        layer = _lambda.LayerVersion.from_layer_version_arn(
            self, 'layer',
            layer_version_arn = 'arn:aws:lambda:'+region+':070176467818:layer:getpublicip:'+number
        )
```

##### af-south-1

```
arn:aws:lambda:af-south-1:070176467818:layer:getpublicip:2
```

##### ap-east-1

```
arn:aws:lambda:ap-east-1:070176467818:layer:getpublicip:2
```

##### ap-northeast-1

```
arn:aws:lambda:ap-northeast-1:070176467818:layer:getpublicip:1
```

##### ap-northeast-2

```
arn:aws:lambda:ap-northeast-2:070176467818:layer:getpublicip:2
```

##### ap-northeast-3

```
arn:aws:lambda:ap-northeast-3:070176467818:layer:getpublicip:2
```

##### ap-south-1

```
arn:aws:lambda:ap-south-1:070176467818:layer:getpublicip:1
```

##### ap-south-2

```
arn:aws:lambda:ap-south-2:070176467818:layer:getpublicip:1
```

##### ap-southeast-1

```
arn:aws:lambda:ap-southeast-1:070176467818:layer:getpublicip:1
```

##### ap-southeast-2

```
arn:aws:lambda:ap-southeast-2:070176467818:layer:getpublicip:1
```

##### ap-southeast-3

```
arn:aws:lambda:ap-southeast-3:070176467818:layer:getpublicip:2
```

##### ca-central-1

```
arn:aws:lambda:ca-central-1:070176467818:layer:getpublicip:2
```

##### eu-central-1

```
arn:aws:lambda:eu-central-1:070176467818:layer:getpublicip:1
```

##### eu-central-2

```
arn:aws:lambda:eu-central-2:070176467818:layer:getpublicip:1
```

##### eu-north-1

```
arn:aws:lambda:eu-north-1:070176467818:layer:getpublicip:2
```

##### eu-south-1

```
arn:aws:lambda:eu-south-1:070176467818:layer:getpublicip:2
```

##### eu-south-2

```
arn:aws:lambda:eu-south-2:070176467818:layer:getpublicip:1
```

##### eu-west-1

```
arn:aws:lambda:eu-west-1:070176467818:layer:getpublicip:1
```

##### eu-west-2

```
arn:aws:lambda:eu-west-2:070176467818:layer:getpublicip:1
```

##### eu-west-3

```
arn:aws:lambda:eu-west-3:070176467818:layer:getpublicip:2
```

##### me-central-1

```
arn:aws:lambda:me-central-1:070176467818:layer:getpublicip:1
```

##### me-south-1

```
arn:aws:lambda:me-south-1:070176467818:layer:getpublicip:2
```

##### sa-east-1

```
arn:aws:lambda:sa-east-1:070176467818:layer:getpublicip:2
```

##### us-east-1

```
arn:aws:lambda:us-east-1:070176467818:layer:getpublicip:1
```

##### us-east-2

```
arn:aws:lambda:us-east-2:070176467818:layer:getpublicip:1
```

##### us-west-1

```
arn:aws:lambda:us-west-1:070176467818:layer:getpublicip:2
```

##### us-west-2

```
arn:aws:lambda:us-west-2:070176467818:layer:getpublicip:1
```
