#!/usr/bin/bash
# Kill all 'ping' processes

lines=$(ps -ax | grep 'ping' | grep -o '^ *[0-9]*')
for line in $lines; do
    kill $line;
done;