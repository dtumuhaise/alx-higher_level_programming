#!/bin/bash
# sends GET request to URL and displays body
curl -sL -w %{http_code} -o /dev/null "$1" && curl -sL "$1"
