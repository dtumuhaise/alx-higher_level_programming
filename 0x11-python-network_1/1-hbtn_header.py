#!/usr/bin/python3
"""
script takes URL, sends request and displays value
of X-REquest-id
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.headers
        request_id = headers.get('X-Request-id')
        print(request_id)
