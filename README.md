# getpublicip

##### Cloud Development Kit (CDK) v2

![awslambda](ICON.png)

```python
        region = Stack.of(self).region

        if region == 'ap-northeast-1' or region == 'ap-south-1' or region == 'ap-southeast-1' or \
            region == 'ap-southeast-2' or region == 'eu-central-1' or region == 'eu-west-1' or \
            region == 'eu-west-2' or region == 'me-central-1' or region == 'us-east-1' or \
            region == 'us-east-2' or region == 'us-west-2' or region == 'eu-central-2': number = str(1)

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

##### eu-north-1

```
arn:aws:lambda:eu-north-1:070176467818:layer:getpublicip:2
```

##### eu-south-1

```
arn:aws:lambda:eu-south-1:070176467818:layer:getpublicip:2
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

##### eu-central-2

```
arn:aws:lambda:eu-central-2:070176467818:layer:getpublicip:1
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
