# encoding = utf-8

import requests
import json
import time


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


url = "http://beta.api.nerve.network/jsonrpc"
headers = {"Content-Type": "application/json"}

sender = "TNVTdTSPNEpLq2wnbsBcD8UDTVMsArtkfxWgz"

passwd = "nuls123456"
amount = 210000\
         * 100000000
remark = "test"
# receiverR = ["TNVTdTSPTXQudD2FBSefpQRkXTyhhtSjyEVAF"]

receiverR = ["TNVTdTSPEgem44Rihm3Dfcjt2JsQj8Gv7Ti5d", "TNVTdTSPW62pTbfi2WLhj96eJKuzuufN2ZweH",
             "TNVTdTSPPLNvD98UZpubMZcn79N9jHp9zugy2", "TNVTdTSPQ4Cqeih2a2rjCAZUGjrg9UPuNjVbq",
             "TNVTdTSPFeCiZFse5JbBPB6Kh6vXKNywSMZra", "TNVTdTSPViRnvQwwACbFt3jGXrRHbnzArT9rU",
             "TNVTdTSPMF5zy7FnKWY5mtryfCGP9CyjXTZ9i", "TNVTdTSPT9cL5AXEqVnW2WeaGY5kjzEeTkvdC",
             "TNVTdTSPPwSttPL8jiprbtxSrw4fDJk6zfAvn", "TNVTdTSPPnSqgzo6zmZvzLiJn9poRKp7mrV4M",
             "TNVTdTSPUTmdXoaZ2gMCsttHGDKeLSstPfi8B", "TNVTdTSPJqqUawEp8h4zScWNjQN6Jkhrh2oSN",
             "TNVTdTSPNRVTRuhNDhQfE5WBRHmB31KwQ2h99", "TNVTdTSPQJDiXSfREgaDCxhDHg5RWuv1MJpaG",
             "TNVTdTSPP5AV2zE1eFvycGZjWmZ9EbjwAEUys", "TNVTdTSPHVuXErqCPjuak7xD3dJVcXoLWHTQV",
             "TNVTdTSPTWGuRcYw2MxPnSR5aFD7ZWqTgeaTx", "TNVTdTSPGkKuAEbScbbzaDdWdjJ6dK5hT6ysV",
             "TNVTdTSPVt8ni6vBhTc4hy6MaeC4G92ncxGDg", "TNVTdTSPTiRkzWj1FvPWJUqp6HPCiMM5aWd8Y",
             "TNVTdTSPGWFtSVGE8GBFExXiRVPCbkSTwmqf5", "TNVTdTSPP2fQMhQtAXXhoTig6Stcm56xhY1HC",
             "TNVTdTSPStMhYR8mpbCQJjad3Xd7EMSkG4Z7Z", "TNVTdTSPJKE5RqxqpxBnXtcvWEd9iMZieCz2w",
             "TNVTdTSPM2EpH7DrKttaqNk3nSQY7mQ7oLy3T", "TNVTdTSPNGzp1M5vfs35K97YEnmhvoJnvx7CV",
             "TNVTdTSPS5kvh5bVf7amiiyFPP9pPPnbxTyP5", "TNVTdTSPKsMZoHQi7v8YrznmZRc9pg91krNkj",
             "TNVTdTSPFH6U488iVPd3BnF2QXDWDEHP1M4Qt", "TNVTdTSPRtbNCS1uuhRGNWjqdsiCKgfmf6EjT",
             "TNVTdTSPJJEoFM6Wy2pkAzeJomUBXu4qPbQzp", "TNVTdTSPJPE4qmyAsAvDu52JVPs685tTGR9dE",
             "TNVTdTSPEqnXW9Rhy3uAR3NGLHcFwZzjxABJj", "TNVTdTSPQXztfyaJU9WyduYsUDkBUoRWbSaYo",
             "TNVTdTSPHHrTDj7ABetDKCqdmR8rGmxSjDeq5", "TNVTdTSPJZFP9joszvdCWXqm2MDqYmqUfxEA9",
             "TNVTdTSPVej3zFKYpRHRhZAR5TQ8a53nQX2sW", "TNVTdTSPLf9qWCZBtcY24FufxQBqD7HVEMs4v",
             "TNVTdTSPQ38RGd55Pr3ZS1sS9XUysUzixg8ps", "TNVTdTSPPXXC7jxHCBgkBHkFpe4r16ynUjKRc"]


def post(url, headers, receiver):

    form_data = {
        "jsonrpc": "2.0",
        "method": "transfer",
        "params": [5, 5, 1, sender, receiver, passwd, amount, remark],
        "id": 1234
    }

    response = requests.post(url, json=form_data, headers=headers)

    # print(response.url)
    # print(response.text)

    # 如果是json文件可以直接显示
    # print(response.json())

    # print(type(response.json()))
    # response1 = response.json()
    print(response.json()["result"]["hash"])
    assert response.json()["result"]["hash"]
    return "Pass"


lenth = len(receiverR)
print(lenth)
for i in range(0, lenth):
    print(receiverR[i], i)
    print(post(url, headers, receiverR[i]))
    time.sleep(1)

# for i in range(0, 9000000):
#     print("第%d次转账:" % i)
#     print(post(url, headers, receiverR[0]))
#     time.sleep(1)


