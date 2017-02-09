# -*- coding:utf-8 -*-	
import urllib.request ,urllib.error
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

author = "<div.*?class=\"author.*?>.*?<a.*?</a>.*?<a.*?>.*?<h2>(.*?)</h2>.*?</a>.*?"
age = "<div.*?class=.*?>(.*?)</div>.*?"
content = "<div.*?class=\"content\".*?<span>(.*?)</span>.*?"
vote = "<span.*?class=\"stats-vote\".*?<i.*?class=\"number\">(.*?)</i>.*?"
comment_num = "<span.*?class=\"stats-comments\".*?<i.*?class=\"number\">(.*?)</i>.*?"
request_attr = author + age + content + vote + comment_num

try:
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile(request_attr,re.S)
    items = re.findall(pattern,content)
    num = 1
    for item in items:
        print("------%s------\nauthor: %s\n\nage: %s\n\ncontent: %s\n\nvote: %s\n\ncomment_num: %s\n" 
        % (num, item[0], item[1], item[2].replace("<br/>","\n"),item[3],item[4]))
        num = num +1
except urllib.error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)