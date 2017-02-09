__author__ = 'limbo'
# -*- coding:utf-8 -*-
import urllib.request
import re

class TB(object):
    #constructor
    def __init__(self,baseUrl,seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)

    #getpage
    def getPage(self,pageNum):
        try:
            url = self.baseUrl + self.seeLZ + '&pn='+str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            return response.read().decode('utf-8')

        except urllib.URLError as e:
            if hasattr(e,"reason"):
                print(e.reason)
            return None

    #getcontent
    def getContent(self,pageNum):
        page = self.getPage(pageNum)
        pattern = re.compile('<div.*?id=\"post_content_.*?>(.*?)<.*?',re.S)
        result = re.search(pattern,page)
        print(result.group(1).strip())

baseUrl = 'http://tieba.baidu.com/p/3138733512'
tb = TB(baseUrl,1)
tb.getContent(1)
