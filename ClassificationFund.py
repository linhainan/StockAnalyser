from DataCatcher import DataCatcher

class fund:
    name=''
    code=''
    parvalue=''
    netvalue=''
    dc=None
    def __init__(self, sno):
        code=str(sno)
        dc = DataCatcher()
        sdic = dc.getdata(code)
        
    def getvalue(self):
        self.value = dc.getdata()
