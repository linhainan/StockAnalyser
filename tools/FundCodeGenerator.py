from Simple_Parser import Simple_Parser
from Simple_WebCatcher import HTMLClient
import json

if __name__ == '__main__':
#    client = HTMLClient()
#    parser = Simple_Parser()
#    fpr = open("classificationfunda.list", 'r')
#    fpw = open("classificationfund.list", 'w')
#    code = fpr.readline()
#    while code:
#        code = code[0:6]
#        webdata = client.GetPage('http://www.jisilu.cn/data/sfnew/detail/'+code, 'utf-8')
#        table = parser.content(webdata, "<table class='tablesorter' style=\"width:100%\">", '</table>') 
#        fundcode = parser.content(table, '<td>', '</td>')
#        fundacode = code
#        fundbcode = str(int(code)+1)
#        fpw.write(fundacode+','+fundbcode+','+fundcode+'\n')
#        code = fpr.readline()
#    fpr.close()
#    fpw.close()
    client = HTMLClient()
    fp = open("classificationfund.list", 'w')
    webdata = client.GetPage('http://www.jisilu.cn/data/sfnew/funda_list/', 'utf-8')
    xml_data = json.loads(webdata)
    table = xml_data["rows"]
    for row in table:
        fp.write(row["id"]+',')
        fp.write(str(int(row["id"])+1)+',')
        fp.write(row["cell"]["funda_base_fund_id"]+',')
        fp.write(row["cell"]["abrate"]+'\n')
    fp.close()


