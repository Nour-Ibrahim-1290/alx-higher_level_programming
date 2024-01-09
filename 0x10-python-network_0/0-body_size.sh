#!/bin/bash
# send a request witha URL and displaynthe size of the response body
curl -s "$1" | wc -c
