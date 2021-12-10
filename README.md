<p align=center><a href="https://learn.srlinux.dev"><img src=https://gitlab.com/rdodin/pics/-/wikis/uploads/0102e45007f7fcc357aacdffe61e9555/srl-ndk-py.svg?sanitize=true/></a></p>

---

The Nokia SR Linux NetOps Development Kit (NDK) allows operators to program high-performance, integrated agents that run alongside the Nokia Service Router Linux (SR Linux).

This repository contains generated Python code for [SR Linux NDK Protocol buffers](https://github.com/nokia/srlinux-ndk-protobufs).

## Installation
The Python `srlinux-ndk` package version is synchronized with the SR Linux [NDK protobuf releases](https://github.com/nokia/srlinux-ndk-protobufs).

Use git tags to check out a particular version of the generated package files.

To install the `srlinux-ndk` python package with `pip`, use one of the following:

```bash
# install the latest version from the main branch
pip install https://github.com/nokia/srlinux-ndk-py/archive/main.zip

# install the specific version from github
pip install https://github.com/nokia/srlinux-ndk-py/archive/0.1.0-rc1.zip
```

These installation steps will install the `srlinux-ndk` package on your system. To import the modules from this package:

```py
from ndk import appid_service_pb2
```

## Code generation
This code has been generated from [SR Linux NDK Protocol buffers](https://github.com/nokia/srlinux-ndk-protobufs) using [`protoc` compiler](https://github.com/srl-labs/protoc-container) with gRPC-Python plugin.

Here is the code generation command that produces the bindings captured in this repo:

> Assuming [`srlinux-ndk-protobufs`](https://github.com/nokia/srlinux-ndk-protobufs) cloned to the home directory **and** checkout out to the needed release/tag.

```bash
docker run -v ~/srlinux-ndk-protobufs:/in -v $(pwd):/out ghcr.io/srl-labs/protoc \
  bash -c "python3 -m grpc_tools.protoc -I /in --python_out=/out --grpc_python_out=/out ndk/*.proto"
```

The python package will appear under `ndk` name in the current working directory.