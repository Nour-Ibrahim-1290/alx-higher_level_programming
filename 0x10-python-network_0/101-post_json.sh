#!/bin/bash
# take URL, sends a JSON POST request, and display the response body.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
