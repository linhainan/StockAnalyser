from tools.MyHTMLParser import XQHTMLParser
from docx import Document
class HTML2Doc:
        def __init__(self):
            self.docfile = ''
        def open(self, docfile):
            doc = Document()
            self.docfile = docfile
            doc.save(docfile)
        def write(self, instream):
            xq_parser = XQHTMLParser(self.docfile)
            xq_parser.complete(instream)
