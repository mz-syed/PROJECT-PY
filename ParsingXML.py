# In this program you will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file. 

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
xml = urllib.request.urlopen(url).read()
print('Retrieved', len(xml), 'characters')
tree = ET.fromstring(xml)

lst = list()
comment = tree.findall('comments/comment')
for count in comment:
    num = count.find('count').text
    lst.append(int(num))

print('Count:', len(lst))
print('Sum:', sum(lst))