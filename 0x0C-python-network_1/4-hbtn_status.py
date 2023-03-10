#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status
You must use the package requests
You are not allow to import packages other than requests"""

import requests

if __name__ == '__main__':

    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)

    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))
