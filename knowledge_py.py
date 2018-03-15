#用来获取api文档的python请求示例
#可能由于网络原因本案例无法返回结果 但适用于python3.6

#coding=utf-8
import socket,urllib.request
import json
import ast
timeout = 5

socket.setdefaulttimeout(timeout)
chaper_url = 'https://api.huobi.pro/market/depth?symbol=ethusdt&type=step1'
# 定义一个网站头UA
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
req = urllib.request.Request(url=chaper_url, headers=headers)
# 输出结果转码utf-8
content = urllib.request.urlopen(req).read().decode('UTF-8')
print(content)
# 上面默认的输出结果是字符串 下面将它转换成字典
json_content = json.loads(content)
tick =json_content['tick']
bids=tick['bids']
print(bids)

