#!/usr/bin/python3
"""
send POST request to passed URL
"""

import sys
import requests


url = sys.argv[1]
email = sys.argv[2]

data = {"email": email}
response = requests.post(url, data=data)

print(response.text)
