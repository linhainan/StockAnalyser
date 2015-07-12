from tools.SinaDataCatcher import SinaDataCatcher
from tools.JisiluDataCatcher import JisiluDataCatcher

classificationfundlist='tools/classificationfund.list'
class fund:
    name=''
    code=''
    parvalue=''
    netvalue=''
    dc=None
    def __init__(self, sno, t):
        code=str(sno)
        if (t == 'a' or t == 'b'):
            dc = SinaDataCatcher()
        else:
            dc = JisiluDataCatcher()
    def getvalue(self):
        self.value = dc.getdata()
