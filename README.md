<p align=center><a href="https://learn.srlinux.dev"><img src=https://gitlab.com/rdodin/pics/-/wikis/uploads/0102e45007f7fcc357aacdffe61e9555/srl-ndk-py.svg?sanitize=true/></a></p>

---

The Nokia SR Linux NetOps Development Kit (NDK) allows operators to program high-performance, integrated agents that run alongside the Nokia Service Router Linux (SR Linux).

This repository contains generated Python code for [SR Linux NDK Protocol buffers](https://github.com/nokia/srlinux-ndk-protobufs).

## Installation
SR Linux NDK follows the SR Linux software version (20.11.1, 21.6.2, etc). For simplicity, the Python package is versioned the same way - v20.11.1, v21.6.2, etc.

Use git tags to checkout a particular version of the generated package files.

To install the `srlinux-ndk` python package with `pip` use one of the following:

```bash
# install the version from the main branch
pip install https://github.com/nokia/srlinux-ndk-py/archive/main.zip

# install the specific version (example given for v21.6.2)
pip install https://github.com/nokia/srlinux-ndk-py/archive/v21.6.2.zip
```

This will install the `srlinux-ndk` package on your system. To import the modules from this package:

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