#!/bin/sh


set -o errexit
set -o nounset

echo twitter stream started . . .

timeout 1m python twitter_app/twitter_stream.py

echo twitter stream finished
sleep 3

echo presto job is started . . .
echo presto job from mysql to mongodb . . .


echo is finished
echo presto job from mysql to hive . . .


echo is finished
echo presto job is finished


exec "$@"
