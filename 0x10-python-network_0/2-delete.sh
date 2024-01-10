#!/bin/bash
# take URL, sends a DELETE request passed as the first argument, and displays the response body.
curl -sX DELETE "$1"
