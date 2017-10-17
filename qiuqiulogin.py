# -*- coding:utf-8 -*-	
import urllib.request ,urllib.error,urllib.parse
import re
import io,sys,time,os

#page = 1
url = 'http://45.115.146.153/login'

headers = { 'Host': '45.115.146.153',
'qqdztype': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'balls/7.4.1 CFNetwork/811.5.4 Darwin/16.7.0',
'Connection': 'keep-alive',
'Connection': 'keep-alive',
'Accept': '*/*',
'Accept-Language': 'zh-cn',
'Content-Length': '424',
'Accept-Encoding': 'gzip, deflate',
'X-Unity-Version': '4.7.2f1'
 }

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

#msg = "尊敬的：(.*?)欢迎来到"
#pattern = re.compile(msg,re.S)
#ld_urls = ['http://t.cn/R6VzYXj','http://t.cn/RiF5ihr',
#    'http://t.cn/Ri893gY','http://t.cn/RtyVl6s','http://t.cn/RJgaRcF']

#for ld_url in ld_urls:
file = open('Request.txt','rb')
try:
     post_data = file.read()
finally:
     file.close()
print(len(post_data))
#print(post_data)
#post_data = 'url'
request = urllib.request.Request(url,post_data,headers = headers)
response = urllib.request.urlopen(request)
content = response.read()  
#item = re.search(pattern,content)
print(content)

os._exit(0)
