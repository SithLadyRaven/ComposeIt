FROM python:3.6-alpine

COPY . /src
WORKDIR /src

RUN pip3 install .

ENTRYPOINT ["ComposeIt"]
