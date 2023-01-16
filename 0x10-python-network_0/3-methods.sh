#!/bin/bash
# displays all HTTP method the server will accept
curl -i -L -X OPTIONS "$1"
