# encoding = utf-8

import requests
import json

def seach(kw):

    kw = {'wd': '长城'}

    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    response = requests.get("http://www.baidu.com/s, params=kw, headers=headers")

    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print("response=", response)

    # 查看响应内容，response.content返回的字节流数据
    print(response.content)

    # 查看完整url地址
    print(response.url)

    # 查看响应头部字符编码
    print(response.encoding)
    # 查看响应码
    print(response.status_code)
    return True


# print(seach("sda"))
url = "http://192.168.1.131:17004/jsonrpc"

headers = {"Content-Type": "application/json"}


def post(url, headers):

    form_data = {
        "jsonrpc": "2.0",
        "method": "transfer",
        "params": [5, 5, 1, "NERVEeTSPVcqUCdfVYWwrbuRtZ1oM6GpSgsgF5", "NERVEeTSPLGfeN8cS9tLBnYnjYjk4MrMabDgcK", "nuls123456", 100000000000, "test"],
        "id": 1234
    }

    response = requests.post(url, json=form_data, headers=headers)

    print(response.url)
    # print(response.text)

    # 如果是json文件可以直接显示
    print(response.json())

    print(type(response.json()))
    # response1 = response.json()
    print(response.json()["result"]["hash"])
    return "Pass"


print(post(url, headers))
