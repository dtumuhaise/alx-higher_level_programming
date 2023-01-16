#!/bin/bash
# displays all HTTP method the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
