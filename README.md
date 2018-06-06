# ComposeIt
[![PyPI version](https://badge.fury.io/py/ComposeIt.svg)](https://badge.fury.io/py/ComposeIt)

Python tool for creating a docker-compose.yml file from an existing container

## Docker image usage
```bash
docker run --rm -ti \
  -v /var/run/docker.sock:/var/run/docker.sock \
  kelsey19/composeit \
  <container id or name>
```

## Installing

```bash
pip install ComposeIt
```

## Usage

```bash
ComposeIt <container id or name>
```

## Options

Option | Description | Default
--- | --- | ---
--socket, -s | docker socket | unix://var/run/docker.sock
