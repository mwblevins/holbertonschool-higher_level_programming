#!/usr/bin/python3
"""Response header value"""

import urllib.request
"""request url lib"""
import sys
"""import sys package"""


url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    x_request_id = headers['X-Request-Id']
    print(x_request_id)
