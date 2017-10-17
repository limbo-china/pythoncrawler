# -*- coding:utf-8 -*-	
import urllib.request ,urllib.error,urllib.parse
import re
import io,sys,time,os

page = 1
url = 'http://www.dianqiuqiu.com'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
headers = { 'Host': 'www.dianqiuqiu.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,zh-CN;q=0.8,zh;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://www.dianqiuqiu.com/',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1' }

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

msg = "尊敬的：(.*?)欢迎来到"
pattern = re.compile(msg,re.S)
ld_urls = ['http://t.cn/R6VzYXj','http://t.cn/RiF5ihr',
    'http://t.cn/Ri893gY','http://t.cn/RtyVl6s','http://t.cn/RJgaRcF']

for ld_url in ld_urls:
    post_data = urllib.parse.urlencode({'url':ld_url }).encode('utf-8')
    request = urllib.request.Request(url,post_data,headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')  
    item = re.search(pattern,content)

os._exit(0)
