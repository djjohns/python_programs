#prompts user to enter file name
fname = raw_input('Please enter a file name: ')
#shortcuts to mbox-short.txt if user presses enter
if len(fname) == 0:
    fname = 'mbox-short.txt'
#uses varible fh to open user given file name
fh = open(fname)
#sets count varible to 0 to be incrmented inside of loop
count = 0
#loops to find all strings starting with the word from
#splits them from the string then parses out wanted data
#prints out all wanted data
#then counts all all instances where string starts with word from
for line in fh:
    if line.startswith('From '):
        line = line.split()
        print line[1]
        count += 1
#prints out count in human readable format
print'There are',count, 'lines in the file with From as the first word'
