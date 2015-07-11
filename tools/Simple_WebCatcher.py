import urllib
import urllib.request
class HTMLClient:
    def GetPage(self, url):
        #user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
        user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36'
        headers = { 'User-Agent' : user_agent }
        req = urllib.request.Request(url, None, headers)
        try:
            res = urllib.request.urlopen(req)
            return res.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            return None
    def GetPic(self, url):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
        headers = { 'User-Agent' : user_agent }
        req = urllib.request.Request(url, None, headers)
        try:
            res = urllib.request.urlopen(req)
            return res.read()
        except urllib.error.HTTPError as e:
            return None
