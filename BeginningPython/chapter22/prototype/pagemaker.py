from xml.sax.handler import ContentHandler
from xml.sax import parse

class PageMaker(ContentHandler):
    passthrough = False
    def startElement(self, name, attrs):
        if name == 'page':
            self.passthrough = True
            self.out = open(attrs['name'] + '.html', 'w')
            self.out.write('<html><head>\n')
            self.out.write(f'<title>{attrs["title"]}</title>')
            self.out.write('</head><body>\n')
        elif self.passthrough:
            self.out.write('<' + name)
            for key,val in attrs.items():
                self.out.write(f' {key}="{val}"')
            self.out.write('>')



    def endElement(self, name):
        if name == 'page':
            self.passthrough = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.passthrough:
            self.out.write('</{}>'.format(name))

    def characters(self, content):
        if self.passthrough:self.out.write(content)


parse('website.xml', PageMaker())