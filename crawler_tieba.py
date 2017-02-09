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
    def getPage(self, pageNum):
        try:
            url = self.baseUrl + self.seeLZ + '&pn='+str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            print(response.read().decode('utf-8'))
            return response

        except urllib.URLError as e:
            if hasattr(e,"reason"):
                print(e.reason)
            return None

baseUrl = 'http://tieba.baidu.com/p/3138733512'
tb = TB(baseUrl,1)
tb.getPage(1)
