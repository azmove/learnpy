#coding=utf-8
import urllib.request
import json,os,datetime
import ast
import sys
while True:
    userInput = input("请输入查询指令 e :")
    if userInput.lower()=="e":
        os.system("clear")
        chaper_url = 'https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=3&tradeType=1&currentPage=1&payWay=&country=&merchant=0&online=1&range=0'
        #定义一个网站头UA
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=chaper_url, headers=headers)
        #输出结果转码utf-8
        content = urllib.request.urlopen(req).read().decode('UTF-8')
        #print(content)
        #上面默认的输出结果是字符串 下面将它转换成字典
        json_content = json.loads(content)
        huoBi_Eth_OTC =json_content['data']
        otc = huoBi_Eth_OTC[0]
        ethotcprice=otc['price']
        ethtradecount = otc['tradeCount']

        chaper_url = 'https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=2&tradeType=1&currentPage=1&payWay=&country=&merchant=0&online=1&range=0'
        # 定义一个网站头UA
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=chaper_url, headers=headers)
        # 输出结果转码utf-8
        content = urllib.request.urlopen(req).read().decode('UTF-8')
        # print(content)
        # 上面默认的输出结果是字符串 下面将它转换成字典
        json_content = json.loads(content)
        huoBi_OTC = json_content['data']
        otc = huoBi_OTC[0]
        #print(otc)

        usdtPrice = otc['price']

        chaper_url = 'https://api.huobi.pro/market/depth?symbol=ethusdt&type=step1'
            # 定义一个网站头UA
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
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
            if  sum(bid) >20:
                asksPrice = bids[i-1][0]
                asksDeep= round(sum(bid),4)
                #print("ETH买入深度：%s   价格：%s USDT"%(asksDeep,asksPrice))
                break

        asks=tick['asks']
        #print("*"*30)
        #print("ASKS:%s"%asks)
        i = 0
        ask =[]
        while i <=19:
            x = asks[i][1]
            i += 1
            ask.append(x)
            if  sum(ask) >20:
                bidsPrice = asks[i-1][0]
                bidsDeep= round(sum(ask),4)
                #print("ETH卖单深度：%s   价格：%s USDT"%(bidsDeep,bidsPrice))
                break

        #print("%s %s %s %s"%(bidsPrice,bidsDeep,asksDeep,asksPrice))
        nowtime =datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("============%s============" %nowtime)
        print("ETH买入深度：%s   价格：%s USDT"%(asksDeep,asksPrice))
        print("+"*40)
        print("+++++++ETH卖出市价：%s RMB++++++++"%(asksPrice*usdtPrice))
        print("+"*40)
        print("当前ETH场外交易买入价格：%s RMB"%ethotcprice)
        swap = asksPrice*usdtPrice-ethotcprice
        print("差价为%s"%(round(swap,4)),end="")
        if  swap>0:
            a=""
            print("%5s交易所内价格高"%a)
        else:
            a=""
            print("%5s场外交易价格高"%a)
        print("场外交易深度%s"%ethtradecount)
        print(" ")
        print("             USDT挂单  USDT:%sRMB              "%usdtPrice)
        print("=" * 44)
        print("单价              数量           用户名")
        for otc in huoBi_Eth_OTC:
            print("%-7s        %-11s      %s" % (otc['price'], otc['tradeCount'], otc['userName']))
        print("=" * 44)
    elif    userInput.lower()=="q":
        exit()
    else:
        continue
