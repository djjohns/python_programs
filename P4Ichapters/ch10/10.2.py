
#prompts user for file name and stores it as 'name'
name = raw_input('PLease enter file name:')

#Shortcuts user to file: mbox-short.txt upon pressing enter
if len(name) < 1 : name = 'mbox-short.txt'

#Try and except insurance to user does not enter invalid file name
try:
    fh = open(name)
except:
    print 'File cound not be opened: ',name
    exit()

#creates dictionary 'counts' to be used in loop
counts = dict()

for loop, parses out data four hours and accumulates counts
for line in fh:    
    if line.startswith('From '): 
        words = line.split()[5].split(':')[0]
        counts[words] = counts.get(words,0) + 1
    
#sorts key and value then flipflops it in the print out for user
for key, val in sorted(counts.items()):
    print key,val
