class Simple_Parser:
    def Parser(self, data, stag, etag):
        epos = 0
        npos = epos
        totallen = 0
        elen = len(etag)
        dlen = len(data)
        depth = 0
        while True:
            epos = data[totallen:].find(etag)
            if epos < 0:
                return -1
            else:
                count = data[totallen:epos+totallen].count(stag)
                depth += count
                depth -=1
                epos += elen
                totallen += epos
                if depth == 0:
                    return totallen
                if totallen >= dlen:
                    return -1
        return -1
    def feed(self, data, stag, etag):
        headtag = stag.split(' ')[0]
        itemList = []
        if not data:
            return  itemlist
        pseek = 0
        while True:
            npos = data[pseek:].find(stag)
            if npos < 0:
                return itemList
        
            nlen = self.Parser(str(data[pseek+npos:]), headtag, etag)
            if nlen >= 0:
                itemList.append(data[pseek+npos:pseek+npos+nlen])
                pseek += npos+nlen
            else:
                return itemList
    def content(self, data, stag, etag):
        headtag = stag.split(' ')[0]
        if not data:
            return  ''
        npos = data.find(stag)
        slen = len(stag)
        elen = len(etag)
        if npos < 0:
            return ''
        nlen = self.Parser(str(data[npos:]), headtag, etag)
        return data[npos+slen:npos+nlen-elen]
    def GetDiv(self, page):
        return self.feed(str(page), 'SNB.data.req_isBrick = 0;', "SNB.data.statusType")
    def GetLink(self, page):
        return self.feed(str(page), "<link", "/>")
    def GetJson(self, page):
        return self.feed(str(page), 'SNB.data.req_isBrick = 0;', "SNB.data.statusType")
