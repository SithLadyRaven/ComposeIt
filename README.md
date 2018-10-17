# ComposeIt
[![](https://images.microbadger.com/badges/image/sithladyraven/composeit.svg)](https://microbadger.com/images/sithladyraven/composeit) [![](https://images.microbadger.com/badges/commit/sithladyraven/composeit:latest.svg)](https://microbadger.com/images/sithladyraven/composeit:latest)

[![GitHub license](https://img.shields.io/github/license/sithladyraven/ComposeIt.svg?style=social)](https://github.com/sithladyraven/ComposeIt/blob/master/LICENSE) [![PyPI version](https://badge.fury.io/py/ComposeIt.svg)](https://badge.fury.io/py/ComposeIt)

Python tool for creating a docker-compose.yml file from an existing container

## Docker image usage
```bash
docker run --rm -ti \
  -v /var/run/docker.sock:/var/run/docker.sock \
  sithladyraven/composeit \
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
