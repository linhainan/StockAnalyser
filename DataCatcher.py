import urllib2
import string

class DataCatcher:
    def getrtdata(self, sno):
        webdata = urllib2.urlopen('http://hq.sinajs.cn/list=' + sno).read().decode('gbk')
        webdata = webdata.split('"')[1]
        if not webdata.strip():
            return None
        data = webdata.split(',')
        stockdata={}
        stockdata["name"] = data[0]
        stockdata["openprice"] = data[1]
        stockdata["yesprice"] = data[2]
        stockdata["curprice"] = data[3]
        stockdata["hprice"] = data[4]
        stockdata["lprice"] = data[5]
        stockdata["jb1"] = data[6]
        stockdata["js1"] = data[7]
        stockdata["amount"] = data[8]
        stockdata["mamount"] = data[9]
        stockdata["b1"] = data[10]
        stockdata["b1price"] = data[11]
        stockdata["b2"] = data[12]
        stockdata["b2price"] = data[13]
        stockdata["b3"] = data[14]
        stockdata["b3price"] = data[15]
        stockdata["b4"] = data[16]
        stockdata["b4price"] = data[17]
        stockdata["b5"] = data[18]
        stockdata["b5price"] = data[19]
        stockdata["s1"] = data[20]
        stockdata["s1price"] = data[21]
        stockdata["s2"] = data[22]
        stockdata["s2price"] = data[23]
        stockdata["s3"] = data[24]
        stockdata["s3price"] = data[25]
        stockdata["s4"] = data[26]
        stockdata["s4price"] = data[27]
        stockdata["s5"] = data[28]
        stockdata["s5price"] = data[29]
        stockdata["date"] = data[30]
        stockdata["time"] = data[31]
        print stockdata["curprice"]
    def surfix(self, no):
        sno = str(no)
        if (int(sno[0:1]) > 5):
            sno = 'sh' + str(no)
        elif (int(sno) == 000001):
            sno = 'sh' + str(no)
        else:
            sno = 'sz' + str(no)
        return sno

if __name__ == '__main__':
    dc = DataCatcher()
    dc.getrtdata(dc.surfix(630010))
