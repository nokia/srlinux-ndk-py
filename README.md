<p align=center><a href="https://learn.srlinux.dev"><img src=https://gitlab.com/rdodin/pics/-/wikis/uploads/0102e45007f7fcc357aacdffe61e9555/srl-ndk-py.svg?sanitize=true/></a></p>

---

The Nokia SR Linux NetOps Development Kit (NDK) allows operators to program high-performance, integrated agents that run alongside the Nokia Service Router Linux (SR Linux).

This repository contains generated Python code for [SR Linux NDK Protocol buffers](https://github.com/nokia/srlinux-ndk-protobufs).

## Installation

The Python `srlinux-ndk` package version is synchronized with the SR Linux [NDK protobuf releases](https://github.com/nokia/srlinux-ndk-protobufs).

Use git tags to check out a particular version of the generated package files.

To install the `srlinux-ndk` python package with `pip`, use one of the following:

```bash
# install the latest version from pypi
pip install srlinux-ndk
# install the specific version from pypi
pip install srlinux-ndk==0.1.0

# install the latest version from the main github branch
pip install https://github.com/nokia/srlinux-ndk-py/archive/main.zip
# install the specific version from github
pip install https://github.com/nokia/srlinux-ndk-py/archive/0.1.0.zip
```

These installation steps will install the `srlinux-ndk` package on your system. To import the modules from this package:

```py
from ndk import appid_service_pb2
```

## Code generation

This code has been generated from [SR Linux NDK Protocol buffers](https://github.com/nokia/srlinux-ndk-protobufs) using [`protoc` compiler](https://github.com/srl-labs/protoc-container) with the gRPC plugins for Go and Python.

`gen.sh` script calls the `protoc` container using the ndk protobufs version as its single argument.

```bash
bash gen.sh v0.1.1
```

The python package will appear under `ndk` name in the current working directory.

## Publishing

To publish the generated package on pypi,

1. Change the version of the package in [setup.py](setup.py) accordingly.
2. Create a github release using UI or gh cli tool.
