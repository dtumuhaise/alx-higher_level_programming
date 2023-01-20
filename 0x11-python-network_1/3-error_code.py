#!/usr/bin/python3
"""
sends a request and displays body response
"""

import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except error.HTTPError as e:
        print("Error code: ", e.code)
