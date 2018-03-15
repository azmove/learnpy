#coding=utf-8
import urllib.request
import json
import ast
import sys

#方式一：直接输出格式为json  例如 coinmarketcap
'''
request = 'https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=3&tradeType=1&currentPage=1&payWay=&country=&merchant=0&online=1&range=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
response = urllib.request.urlopen(request)
coinmarketcap = json.load(req)
print("币种       价格 ")
for x in coinmarketcap:

    print("%s       %s"%(x['price'],x['userName']))
'''
#方式二：URL输出是字典 包含字典的方式
#定义一个网址变量
chaper_url = 'https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=3&tradeType=1&currentPage=1&payWay=&country=&merchant=0&online=1&range=0'
#定义一个网站头UA
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=chaper_url, headers=headers)
#输出结果转码utf-8
content = urllib.request.urlopen(req).read().decode('UTF-8')
#print(content)
#上面默认的输出结果是字符串 下面将它转换成字典
json_content = json.loads(content)
huoBi_OTC =json_content['data']
otc = huoBi_OTC[1]
print("="*44)
print("                 ETH挂单                ")
print("="*44)
print("单价              数量           用户名")
for otc in  huoBi_OTC:
    print("%-7s        %-11s      %s"%(otc['price'],otc['tradeCount'],otc['userName']))
print("="*44)




#遍历key value值
'''
for key,value in new.items():
    print(key,value)
'''