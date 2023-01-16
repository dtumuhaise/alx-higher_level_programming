#!/bin/bash
# send request to URL and displays only status code
curl -w "%{http_code}" "$1"
