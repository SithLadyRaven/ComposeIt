FROM python:3.6-alpine

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/rossf7/label-schema-automated-build.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1"

COPY . /src
WORKDIR /src

RUN pip3 install .

ENTRYPOINT ["ComposeIt"]
