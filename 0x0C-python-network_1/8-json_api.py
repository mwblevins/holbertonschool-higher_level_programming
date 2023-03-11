#!/usr/bin/python3
"""Write a Python script that takes
in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    response = requests.post('http://0.0.0.0:5000/search_user', data={"q": q})
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
