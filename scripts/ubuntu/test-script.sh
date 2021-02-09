#!/bin/bash

echo "Hello world!"
echo $0
echo $1

ROOT=$(dirname $0)/..
PYTHON=$ROOT/env/bin/python
echo $ROOT
echo $PYTHON