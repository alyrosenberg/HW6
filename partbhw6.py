#part B of HW6
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Delilah.html'
count = 7
position = 18

for x in range(int(count)):
	html = urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')
	tags = soup('a')
	number = 0
	for tag in tags:
		number += 1
		if number == int(position):
			url = tag.get('href')
			if x == int(count)-1:
				print (tag.contents[0])

