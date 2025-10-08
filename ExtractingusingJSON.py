# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file


import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL: ')
print('Retrieving', url)
try:
    jason_file = urllib.request.urlopen(url)
    data = jason_file.read()
except:
    print('Invalid URL - Redirecting to correct URL for this assignment...\n---> http://py4e-data.dr-chuck.net/comments_2307381.json')
    url = 'http://py4e-data.dr-chuck.net/comments_2307381.json'
    print('Retrieving', url)

    jason_file = urllib.request.urlopen(url)
    data = jason_file.read()

print('Retrieved',(len(data)), 'characters in JSON file.')

try:
    info = json.loads(data)
except:
    info = None

if not info:
    print('Failed to retrieve data')

num_list = list()
for item in info['comments']:
    count = item['count']
    num_list.append(count)

print('Total comments in File:', len(num_list))
print('Sum of all counts in comments :', sum(num_list))

