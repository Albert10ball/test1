# encoding = utf-8

import requests

url = "http://beta.nervedex.com/api/tradings"
headers = {"Content-Type": "application/json"}


def get_tradings(url, headers):

    response = requests.get(url, headers=headers)
    print(response.text)
    return response.json()


res = get_tradings(url, headers)
print(res["data"][0]["symbol"])


