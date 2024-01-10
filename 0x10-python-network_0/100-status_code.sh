#!/bin/bash
# take URL, sends a request, and display only the status code of the response.
curl -s -L -X HEAD -w "%{http_code}" "$1"
