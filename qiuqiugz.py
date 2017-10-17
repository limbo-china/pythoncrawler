# -*- coding:utf-8 -*-	
import urllib.request ,urllib.error,urllib.parse
import re
import io,sys,time,os

#page = 1
url1 = 'http://45.115.146.153/game'
url2 = 'http://45.115.146.153/msg'

headers1 = { 'Host': 'acc.battleofballs.com',
'qqdztype': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'balls/7.4.1 CFNetwork/811.5.4 Darwin/16.7.0',
'Connection': 'keep-alive',
'Connection': 'keep-alive',
'Accept': '*/*',
'Accept-Language': 'zh-cn',
'Content-Length': '104',
'Accept-Encoding': 'gzip, deflate',
'X-Unity-Version': '4.7.2f1'
 }
headers2 = { 'Host': 'acc.battleofballs.com',
'qqdztype': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'balls/7.4.1 CFNetwork/811.5.4 Darwin/16.7.0',
'Connection': 'keep-alive',
'Connection': 'keep-alive',
'Accept': '*/*',
'Accept-Language': 'zh-cn',
'Content-Length': '40',
'Accept-Encoding': 'gzip, deflate',
'X-Unity-Version': '4.7.2f1'
}
headers3 = { 'Host': 'acc.battleofballs.com',
'qqdztype': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'balls/7.4.1 CFNetwork/811.5.4 Darwin/16.7.0',
'Connection': 'keep-alive',
'Connection': 'keep-alive',
'Accept': '*/*',
'Accept-Language': 'zh-cn',
'Content-Length': '56',
'Accept-Encoding': 'gzip, deflate',
'X-Unity-Version': '4.7.2f1'
 }

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

#msg = "尊敬的：(.*?)欢迎来到"
#pattern = re.compile(msg,re.S)
#ld_urls = ['http://t.cn/R6VzYXj','http://t.cn/RiF5ihr',
#    'http://t.cn/Ri893gY','http://t.cn/RtyVl6s','http://t.cn/RJgaRcF']

#for ld_url in ld_urls:
file1 = open('Request2.txt','rb')
file2 = open('Request3.txt','rb')
file3 = open('Request4.txt','rb')
file4 = open('Request5.txt','rb')
try:
     post_data1 = file1.read()
finally:
     file1.close()
print(len(post_data1))

try:
     post_data2 = file2.read()
finally:
     file2.close()
print(len(post_data2))
try:
     post_data3 = file3.read()
finally:
     file3.close()
print(len(post_data3))
try:
     post_data4 = file4.read()
finally:
     file4.close()
print(len(post_data4))
#print(post_data1)
#post_data = 'url'
request1 = urllib.request.Request(url1,post_data1,headers = headers1)
response = urllib.request.urlopen(request1)

request2 = urllib.request.Request(url2,post_data2,headers = headers2)
response = urllib.request.urlopen(request2)

request3 = urllib.request.Request(url2,post_data3,headers = headers3)
response = urllib.request.urlopen(request3)

request4 = urllib.request.Request(url2,post_data4,headers = headers3)
response = urllib.request.urlopen(request4)
#content = response.read()  
#item = re.search(pattern,content)
#print(content)

os._exit(0)
