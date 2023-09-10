# get-public-ip

 - https://github.com/aws-samples/aws-lambda-extensions/tree/main/s3-logs-extension-demo-container-image

### Short

Capture the Public IP Address during a Lambda Container execution for correlation against Cloud Trail logs.

### About

Source Code: [https://github.com/4n6ir/getpublicip](https://github.com/4n6ir/getpublicip)

Maintainer: [John Lukach](https://lukach.io)

### Usage

The extension requires these lines to be added to the ```Dockerfile``` for the Lambda Cotainer.

```docker
FROM public.ecr.aws/p4b7o4r9/getpublicip:latest AS layer
```

```docker
WORKDIR /opt
COPY --from=layer /opt/ .
```
