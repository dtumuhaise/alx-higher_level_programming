#!/bin/bash
# send request to URL and displays only status code
curl -sLw "%{http_code}" -o /dev/null "$1"
