# Use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter the URL to parse: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

num_list = list()
tags = soup('span')
for tag in tags:
    nums = int((tag.contents[0]))
    num_list.append(nums)

print(sum(num_list))



