#!/bin/bash
# sends request to URL and displays size of body of response
curl -sL "$1" | awk '{print length}'
