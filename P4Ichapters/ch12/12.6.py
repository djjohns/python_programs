import urllib
import xml.etree.ElementTree as ET

#Prompts user to enter URL 
url = raw_input('Enter URL - ')

#Shortcuts user to specified webpage upon pressing enter
if len(url) < 1 : url =  'http://python-data.dr-chuck.net/comments_42.xml'

#Url handler to open and read the given URL
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()

print 'Retrieved',len(data),'characters'
#Looks through all the <comment> tags and find the <count> values
#to sum the numbers
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print 'Count:', len(counts)
total = 0
for comment in tree.findall("./comments/comment"):
    total += int(comment.find('count').text)
print total
