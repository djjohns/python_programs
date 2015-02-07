counts = dict()
names = ['name']
for name in names :
    if name not in counts:
        counts[name]= 1
    else:
        counts[name] = counts[name]+1
print counts



#creates or updates count dictionary
counts = dict()
names = ['name']
for name in names:
    counts[name]=counts.get(name,0)=1
print counts



#counting pattern
counts = dict()
print 'Enter a line of text'
line = raw_input('')
#splits input into a list
words = line.split()
print 'Words:',words
#counts how many times each word occurs
print 'counting...'
for word in words:
    counts[word]=counts.get(words,0)+1

print 'Counts', counts
