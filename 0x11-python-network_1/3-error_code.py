#!/usr/bin/python3
"""
sends a request and displays body response
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
