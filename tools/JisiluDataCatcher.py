from tools.Simple_WebCatcher import HTMLClient
import json

class JisiluDataCatcher:
    def getdata(self, code):
        webdata = HTMLClient().GetPage("http://www.jisilu.cn/jisiludata/StockFenJiDetail.php?qtype=hist&display=table&fund_id="+code, 'utf-8')
        table_content = json.loads(webdata)["rows"]
        return table_content[0]
    def getvalue(self, code):
        return self.getdata(code)["cell"]["net_value"]

if __name__ == '__main__':
    print(JisiluDataCatcher().getdata('161022'))
