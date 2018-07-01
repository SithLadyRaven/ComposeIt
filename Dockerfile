FROM python:3.6-alpine

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="ComposeIt" \
      org.label-schema.description="Create docker-compose.yml from existing containers" \
      org.label-schema.vcs-url="https://github.com/kelsey19/ComposeIt" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0"

COPY . /src
WORKDIR /src

RUN pip3 install .

ENTRYPOINT ["ComposeIt"]
