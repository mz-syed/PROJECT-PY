# To retrieve web pages from servers as dictionary and count the words using urllib library to connect sockets for using HTTP protocol

import urllib.request, urllib.parse, urllib.error

handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in handle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)
