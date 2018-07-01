# ComposeIt
[![](https://images.microbadger.com/badges/image/kelsey19/composeit.svg)](https://microbadger.com/images/kelsey19/composeit) [![](https://images.microbadger.com/badges/commit/kelsey19/composeit:latest.svg)](https://microbadger.com/images/kelsey19/composeit:latest)

[![GitHub license](https://img.shields.io/github/license/kelsey19/ComposeIt.svg?style=social)](https://github.com/kelsey19/ComposeIt/blob/master/LICENSE) [![PyPI version](https://badge.fury.io/py/ComposeIt.svg)](https://badge.fury.io/py/ComposeIt)

Python tool for creating a docker-compose.yml file from an existing container

## Docker image usage
```bash
docker run --rm -ti \
  -v /var/run/docker.sock:/var/run/docker.sock \
  kelsey19/composeit \
  <container id or name> <container id or name> ...
```

## Installing from source
```bash
python3 setup.py install --user
```

## Installing with pip

```bash
pip3 install ComposeIt
```

## Usage

```bash
ComposeIt <container id or name> <container id or name> ...
```

## Options

Option | Description | Default
--- | --- | ---
--socket, -s | docker socket | unix://var/run/docker.sock
