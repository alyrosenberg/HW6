#alyson rosenberg hw6

#part A of the homework 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen('http://py4e-data.dr-chuck.net/comments_36098.html', context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
spans = soup('span')
numbs = []

for span in spans:
	numbs.append(int(span.string))

print (sum(numbs))


