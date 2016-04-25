import urllib
import re
from bs4 import *
sum=0
#Prompts user to enter URL 
url = raw_input('Enter URL - ')

#Shortcuts user to specified webpage upon pressing enter
if len(url) < 1 : url =  'http://python-data.dr-chuck.net/comments_42.html'

#try and except to handle invalid or down server
try:
    html = urllib.urlopen(url).read()
except:
    print 'Host could not be reached' ,url
    exit()


soup = BeautifulSoup(html,"html.parser")

# Retrieve all of the specified tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    ExtractedTags=str(tag)
    TagSearch= re.findall("[0-9]+",ExtractedTags)
    for TagCount in TagSearch:
        TagCount=int(TagCount)
        sum=sum+TagCount
print 'Sum:',sum
print 'Count:' ,TagCount


