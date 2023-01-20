#!/usr/bin/python3
"""
sends a request and displays body response
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
