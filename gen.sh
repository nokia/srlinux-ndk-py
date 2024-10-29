#!/bin/bash

# usage: bash gen.sh <protobufVersion>, where protobufVersion is the tag of the protobufs repo
# example: bash gen.sh v0.2.0

set -e

PROJ_DIR=$(pwd)

# dir where proto files are located
# must be cloned from https://github.com/nokia/srlinux-ndk-protobufs
PROTO_DIR=~/nokia/srlinux-ndk-protobufs

# tag matching the protobuf tag in the https://github.com/nokia/srlinux-ndk-protobufs
# from which the Python bindings are about to be generated
PROTO_VER=$1

if [ -z "$1" ]; then
    echo "protobufs version from which to generate bindings is not set. usage: bash gen.sh <protobufVersion>."
    exit 1
fi

# remove previously generated bindings
sudo rm -rf ${PROJ_DIR}/ndk

# checkout protos to the desired version
cd ${PROTO_DIR} && git checkout refs/tags/${PROTO_VER}

PROTOC_IMAGE=ghcr.io/srl-labs/protoc:24.4__1.31.0

docker run -v ${PROTO_DIR}:/in -u $(id -u):$(id -g) -v ${PROJ_DIR}:/out ${PROTOC_IMAGE} \
  ash -c "python3 -m grpc_tools.protoc -I /in --python_out=/out --grpc_python_out=/out ndk/*.proto"

# replace version number in setup.py with PROTO_VER

sed -i "s/version=.*/version=\"${PROTO_VER:1}\",/g" ${PROJ_DIR}/setup.py


# once the bindings are generated, we can push it to the repo
# git push
# and create a release
# gh release create v0.2.0 --generate-notes