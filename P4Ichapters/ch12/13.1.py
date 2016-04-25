import urllib
from BeautifulSoup import *

url = raw_input('Enter URL : ')
position = raw_input('Enter position : ')
count = raw_input('Enter count : ')


uh = urllib.urlopen(url)
data = uh.read()
soup = BeautifulSoup(data)

# Retrieve all of the anchor tags
tags = soup('a')

links = list()

#grabs href tag of specified link
for tag in tags:
    links.append(tag.get('href', None))

print 'Retrieving: ', links[0]
print 'Retrieving: ', links[int(position)-1]

#link posistion and counter
link = links[int(position)-1]
counter = 1
while counter < int(count):
    uh = urllib.urlopen(link)
    data = uh.read()
    soup = BeautifulSoup(data)

    # Retrieve all of the anchor tags
    tags = soup('a')

    links = list()

    for tag in tags:
        links.append(tag.get('href', None))
    print 'Retrieving: ', links[int(position)-1]
    link = links[int(position)-1]
    counter = counter + 1
