#!/usr/bin/python3
"""
Python script that takes 2 arguments in
order to solve this challenge.
"""

import sys
import requests


if __name__ == "__main__":

    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)
    response = requests.get(url)
    commits = response.json
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
