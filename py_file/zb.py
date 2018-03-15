#coding=utf-8
import urllib.request
import json,os
import ast
import sys

chaper_url = 'https://trans.zb.com/line/topall?jsoncallback=jQuery19103531945619331822_1518767974302&_=1518767974304'
    # 定义一个网站头UA
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
req = urllib.request.Request(url=chaper_url, headers=headers)
# 输出结果转码utf-8
content = urllib.request.urlopen(req).read().decode('UTF-8')
# print(content)
# 上面默认的输出结果是字符串 下面将它转换成字典
contents = content.lstrip('jQuery19103531945619331822_1518767974302(')
content =contents.rstrip(')')
print(content)
print(type(contents))
json_content = json.loads(content)
print(type(json_content))
datas =json_content['datas']
print(datas)
print(datas[4])
for a in datas:
    print("%-10s %-5s %s "%(a['market'],a['currrency'],a['lastPrice']))

