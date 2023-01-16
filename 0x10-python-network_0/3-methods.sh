#!/bin/bash
# displays all HTTP method the server will accept
curl -X OPTIONS "$1"
