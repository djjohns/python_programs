
#asks for file to store in varible name, the uses varible handle to open file
#varible text reads file and varible word split it into a list
name = raw_input('Enter file:')
handle = open(name, 'r')
text = handle.read()
words = text.split()
#sets up the count dictionary
counts = dict()
for word in words:
    counts[word]=counts.get(word,0)+1
#Sets up largest word and count loop
bigcount = None
bigword = None
for word,count in counts.item():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
#prints the largest found for user
print bigword,bigcount
