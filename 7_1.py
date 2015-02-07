fname = raw_input ('Please enter the file name:')
try:
    hfile = open('fname')
    
except:
    print'File could not be opened, please enter a valid file name:',fname
    exit()

for line in hfile:
        new_line = line.upper()
        print new_line
        quit ()


