from Simple_WebCatcher import HTMLCient
import json

class JisiluDataCatcher:
    def getdata(self, code):
        webdata = HTMLClient().getGetPage("http://www.jisilu.cn/jisiludata/StockFenJiDetail.php?qtype=hist&display=table&fund_id="+code, 'utf-8')
        table_content = json.loads(webdata)["rows"]
        return table_content[0]
