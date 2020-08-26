# encoding = utf-8

import requests
import learn.any_time

url = "http://beta.nervedex.com/api/time"
headers = {"Content-Type": "application/json"}


def get_time(url, headers):
    response = requests.get(url, headers=headers)
    return response.json()


time = get_time(url, headers)["data"]
print(time)


