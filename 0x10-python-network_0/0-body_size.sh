#!/bin/bash
# Bash script that shows the byte size of the  response header for a given URL.
curl -s "$1" | wc -c
