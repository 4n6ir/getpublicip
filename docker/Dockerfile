### 2.143.1 (build 29b0d66) ###

FROM python:3.8-alpine AS installer

COPY src /opt/
COPY src/requirements.txt /opt/
RUN pip install -r /opt/requirements.txt -t /opt/extensions/lib
WORKDIR /opt/extensions
RUN chmod -R 755 *.py

FROM scratch AS base
WORKDIR /opt/extensions
COPY --from=installer /opt/extensions .