#!/bin/bash

line="-----------------------------------"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; whoami; echo $line

echo "Public IP"; curl icanhazip.com; echo $line

echo "Finishing at: $(date)"