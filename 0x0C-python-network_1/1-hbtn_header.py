#!/usr/bin/python3
"""Response header value"""

import urllib.request
"""_summary_"""
import sys
"""_summary_"""


url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    x_request_id = headers['X-Request-Id']
    print(x_request_id)
