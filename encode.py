import sys
from BeautifulSoup import BeautifulStoneSoup

def unescape(s):
 return BeautifulStoneSoup(s, smartQuotesTo="html")

if __name__ == "__main__":
  for row in sys.stdin:
    row = row.strip()
#    print row, type(row)
    row = row.decode("utf-8")
#    print row, type(row)
    print row.encode("ascii", 'xmlcharrefreplace')
#    result = unescape(row)
#    print result
