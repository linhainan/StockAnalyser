from tools.SinaDataCatcher import SinaDataCatcher
from tools.JisiluDataCatcher import JisiluDataCatcher
from tools.FundCodeGenerator import Fundlist
import decimal
import time, threading

classificationfundlist='tools/classificationfund.list'
class fund:
    name=''
    code=''
    parvalue=0
    netvalue=0
    dc=None
    def __init__(self, sno, t):
        code=str(sno)
        if (t == 'a' or t == 'b'):
            self.dc = SinaDataCatcher()
            #self.name = self.dc.getname(code)
        else:
            self.dc = JisiluDataCatcher()
            self.netvalue = decimal.Decimal(self.dc.getvalue(code))
        self.code=code
    def getvalue(self):
        value = self.dc.getvalue(self.code)
        if value.strip():
            return decimal.Decimal(value)
        return decimal.Decimal('1')

class classificationfund:
    funda=None
    fundb=None
    fund=None
    abrate=0.5
    def __init__(self, codea, codeb, codef, abrate):
        self.funda = fund(codea, 'a')
        self.fundb = fund(codeb, 'b')
        self.fund = fund(codef, 'f')
        self.abrate = decimal.Decimal(abrate)
    def overrate(self, limit):
        rate = 0
        if self.fund.netvalue > decimal.Decimal(0):
            rate = (self.funda.getvalue() * self.abrate + self.fundb.getvalue() * (1 - self.abrate)- self.fund.netvalue) / (self.fund.netvalue)
        if rate < decimal.Decimal(limit):
            print('Funda Code: '+self.funda.code+',rate '+ str(rate))

def workperiod(nowh, nowm, starth, startm, endh, endm):
    delta = 0
    if nowh > endh:
        delta = (24 - nowh + starth) * 3600 + (startm - nowm) * 60
    elif nowh < starth:
        delta = (starth - nowh) * 3600 + (startm - nowm) * 60
    else:
        delta = 30
    if delta > 0:
        return delta
    return 0

def alarmprog(cfundlist):
    print("Alarm Clock Starting...")
    while True:
        t = time.localtime()
        delta = workperiod(t.tm_hour, t.tm_min, 9, 0, 15, 0)
        time.sleep(delta)
        for fund in cfundlist:
            fund.overrate('-0.02')
def updateprog(cfundlist):
    while True:
        t = time.localtime()
        delta = 0
        if t.tm_hour == 9:
            print("Updating the Fund net value...")
            for fund in cfundlist:
                fund.fund.netvalue = fund.fund.getvalue()
        if t.tm_hour >= 9:
            delta = (24 - t.tm_hour + 9) * 3600 + (0 - t.tm_min) * 60
        if t.tm_hour < 9:
            delta = (9 - t.tm_hour) * 3600 + (0 - t.tm_min) * 60
        time.sleep(delta)


if __name__ == '__main__':
    #Fundlist().init('tools/classificationfund.list')
    fp = open('tools/classificationfund.list', 'r')
    row = fp.readline()
    cfundlist=[]
    while row:
        cell = row.split(',') 
        a = int(cell[3].split(':')[0])
        b = int(cell[3].split(':')[1])
        f = classificationfund(cell[0], cell[1], cell[2], str(a/(a+b)))
        cfundlist.append(f)
        row = fp.readline()
    fp.close()
    threading.Thread(target=alarmprog,args=(cfundlist,)).start()
    threading.Thread(target=updateprog,args=(cfundlist,)).start()
