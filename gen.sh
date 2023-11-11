#!/bin/sh

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
rm -rf ${PROJ_DIR}/ndk

# checkout protos to the desired version
cd ${PROTO_DIR} && git checkout ${PROTO_VER}

docker run -v ${PROTO_DIR}:/in -v ${PROJ_DIR}:/out ghcr.io/srl-labs/protoc:23.3__1.31.0 \
  ash -c "python3 -m grpc_tools.protoc -I /in --python_out=/out --grpc_python_out=/out ndk/*.proto"


# once the bindings are generated, we can push it to the repo
# git push
# and create a release
# gh release create v0.2.0 --generate-notes