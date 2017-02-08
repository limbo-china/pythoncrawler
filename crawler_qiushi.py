# -*- coding:utf-8 -*-	
import urllib.request ,urllib.error
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>.*?<h2>(.*?)</h2>.*?</a>.*?<div.*?class'+
                     '="content".*?<span>(.*?)</span>',re.S)
    items = re.findall(pattern,content)
    num = 1
    for item in items:
        print("%s: author: %s\n  content: %s" % (num, item[0], item[1]))
        num = num +1
except urllib.error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)