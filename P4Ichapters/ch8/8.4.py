#propts user for file name
fname = raw_input('Please enter a file name: ')
#shortcuts to romeo.txt if user presses enter upon prompt
if len(fname) == 0:
    fname = 'romeo.txt'
#assigns varible fhandle to open the usper input file name
fhandle= open(fname)
#creates a list stored as lstone
lstone = []
#loops to read lines, split lines,checks list to see if words are in lstone,
#if not in lstone;adds to lst one, then sorts alphabeticaly
for line in fhandle:
    line = line.split()
    for words in line:
        if words in lstone:continue
        lstone.append(words)
        lstone.sort()
#prints lstone 
print lstone
