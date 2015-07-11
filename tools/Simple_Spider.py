import re
import urllib
import urllib.request
import time
import string
import json

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.attrs = []
 
    def handle_starttag(self, tag, attrs):
        if tag == "div":
            if len(attrs) == 0: pass
            else:
                self.attrs = attrs
                for (variable, value)  in attrs:
                    if variable == "class":
                        if value == "ImgSearch":
                            print('find')
    def handle_data(self, data):
        print(data)
        attrs = self.attrs
        for (variable, value)  in attrs:
            if variable == "class":
                if value == "ImgSearch":
                    print("data"+data)

class MyParser:
    def __init__(self):
        self.enable = True
        self.begin = 0
        self.end = 0
        self.dep = 0
        #self.MyTool = HTML_Tool()
    def Parser(self, data, stag, etag):
        epos = 0
        npos = epos
        totallen = 0
        elen = len(etag)
        dlen = len(data)
        self.dep = 0
        while True:
            epos = data[totallen:].find(etag)
            print("len" +str(epos))
            #print(repr(data[npos:npos+epos]))
            print(self.dep)
            #print(repr(data[npos]))
            if epos < 0:
                return -1
            else:
                count = data[totallen:epos+totallen].count(stag)
                self.dep += count
                print(count)
                self.dep -=1
                epos += elen
                totallen += epos
                if self.dep == 0:
                    return totallen
                if totallen >= dlen:
                    return -1
        return -1
    def getElem(self, tag):
        return tag.split(' ')[0]
    def feed(self, data, stag, etag):
        #data = self.MyTool.Replace_Char(str(data))
        headtag = self.getElem(stag)
        itemList = []
        pseek = 0
        while True:
            npos = data[pseek:].find(stag)
            #print(data[npos:1000])
            if npos < 0:
                return itemList
        
            nlen = self.Parser(str(data[pseek+npos:]), headtag, etag)
                #print(data)
                #print(data[npos:])
            if nlen >= 0:
                #print(len(data[npos:nlen+npos]))
                #self.savefile(bytes(data[npos:npos+nlen], "UTF-8"))
                itemList.append(data[pseek+npos:pseek+npos+nlen])
                pseek += npos+nlen
            else:
                #print(data[npos:])
                #self.savefile(bytes(data[npos:], "UTF-8"))
                #itemList.append(data[pseek+npos:])
                return itemList
        
            

class Simple_Spider:
    def __init__(self, url, filename, sflag, eflag):
        self.done = False
        self.sflag = sflag
        self.eflag = eflag
        self.fname = filename
        self.url = url
    def GetDiv(self, page):
        #ps = self.sflag + "(.*?)" + self.eflag
        #print(self.sflag)
        #pat = re.compile(r'<div class="ImgSearch"(.*)>(.*?)</div>', re.DOTALL)
        #items = pat.findall(page)
        #self.savefile(bytes(self.sflag, 'UTF-8'))
        #(items)
        #for item in items:
        #    print(item[0])
        #    io = input()
        #    self.savefile(bytes(item, 'UTF-8'))
        #self.savefile(bytes(self.eflag, 'UTF-8'))
        mypaser = MyParser()
        #<div id="status_content" class="status_content container active tab-pane">
        #<div class="statuses_container container tab-content"
        return mypaser.feed(str(page), 'SNB.data.req_isBrick = 0;', "SNB.data.statusType")
    def GetLink(self, page):
        mypaser = MyParser()
        return mypaser.feed(str(page), "<link", "/>")
    def GetJson(self, page):
        mypaser = MyParser()
        return mypaser.feed(str(page), 'SNB.data.req_isBrick = 0;', "SNB.data.statusType")
    def GetPage(self, url):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
        headers = { 'User-Agent' : user_agent }
        req = urllib.request.Request(url, None, headers)
        res = urllib.request.urlopen(req)
        print(req)
        return res.read().decode("utf-8")
    def Start(self):
        page = self.GetPage(self.url)
        
        #divList = self.GetDiv(page)
        #linkList = self.GetLink(page)
        jsonList = self.GetJson(page)
        ijson = jsonList[0]
        s = ijson.find('{')
        e = ijson.rfind('}')
        ijson = ijson[s:e+1]
        print (json.loads(ijson)["statuses"][0]["description"])
        #print (ijson)
        with open('index1.html', 'wb') as outfile:
            outfile.write(bytes(jsonList[0], 'UTF-8'))
        #    outfile.write(b'<head>')
        #    outfile.write(b'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
        #    for json in jsonList:
        #        outfile.write(bytes(link, "UTF-8"))
        #    outfile.write(b'</head>')
        #    for div in divList:
        #        outfile.write(bytes(div, "UTF-8"))
        outfile.close()
        cmd = input()

#tag = '<div class="news_list news_list02">'
#print (tag.split(' ')[0])
#mySpider = Simple_Spider("http://xw.jx3.xoyo.com/news/", "jx3.html", '<div class="news_list news_list02">', u'</div>')
#mySpider.Start()
mySpider = Simple_Spider("http://xueqiu.com/2821861040", "jx3.html", '<div class="news_list news_list02">', u'</div>')
mySpider.Start()
