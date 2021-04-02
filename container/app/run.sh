#!/bin/sh


set -o errexit
set -o nounset

sleep 10


exec "$@"
