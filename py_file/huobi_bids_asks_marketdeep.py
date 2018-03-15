#coding=utf-8
import socket,urllib.request
import json,os
import ast
import sys
timeout = 5
socket.setdefaulttimeout(timeout)
chaper_url = 'https://api.huobi.pro/market/depth?symbol=ethusdt&type=step1'
    # 定义一个网站头UA
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
req = urllib.request.Request(url=chaper_url, headers=headers)
# 输出结果转码utf-8
content = urllib.request.urlopen(req).read().decode('UTF-8')
# print(content)
# 上面默认的输出结果是字符串 下面将它转换成字典
json_content = json.loads(content)
tick =json_content['tick']
bids=tick['bids']
#print(bids)
#bids[第一个][第二列]
i = 0
bid =[]
while i <=19:
    x = bids[i][1]
    i += 1
    bid.append(x)
    if  sum(bid) >10:
        asksPrice = bids[i-1][0]
        asksDeep= round(sum(bid),4)
        print("BID买入大于10对应的深度是：%s   对应的价格为：%s"%(asksDeep,asksPrice))
        break


asks=tick['asks']
print("\b")
print("*"*30)
#print("ASKS:%s"%asks)
i = 0
ask =[]
while i <=19:
    x = asks[i][1]
    i += 1
    ask.append(x)
    if  sum(ask) >10:
        bidsPrice = asks[i-1][0]
        bidsDeep= round(sum(ask),4)
        print("BID卖单大于10对应的深度是：%s   对应的价格为：%s"%(bidsDeep,bidsPrice))
        break

print("%s %s %s %s"%(bidsPrice,bidsDeep,asksDeep,asksPrice))