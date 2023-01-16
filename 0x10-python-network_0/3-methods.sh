#!/bin/bash
# displays all HTTP method the server will accept
curl -s -X OPTIONS "$1" | grep "Allow" | cut -d " " -f2-
