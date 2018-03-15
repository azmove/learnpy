#coding=utf-8

#遍历字符串并统计每个字符显示的次数
str = "hello world"
for x in str:
    times = str.count(x)
    if x ==" ":
        continue
    print("%s %s"%(x,times))