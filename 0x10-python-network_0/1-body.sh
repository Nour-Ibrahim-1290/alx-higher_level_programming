#!/bin/bash
# take URL, sends a GET request, and displays the response body only of status-code 200 OK
curl -sL "$1"
