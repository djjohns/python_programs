#propmts user for file name,
#if user presses enter program will open mbox_short
name = raw_input('Enter file:')
if len(name) < 1 : name = 'mbox-short.txt'
#Program trys to open users input 
try:
    fh = open(name)
#Program will print out if file could not be opened in the event of #bad input
#then exits program
except:
    print 'File could not be opened:',name
    exit()
#sets up the varibles for the dictionaries and list to be used
counts = dict()
emails = list()
#For loop to parse out and strip unwanted data
#then increments count of email addresses or creates new for the count
for line in fh:
    line = line.rstrip()
    words = line.split()
    if line.startswith ('From '):
        emails = words[1]
        counts[emails] = counts.get(emails,0) + 1
#For loop to find largest ammount of emails sent from one user
#then prints the most re-curring email adn how many times the address #appears
bigcount = None
bigword = None
for words,emails in counts.items():
    if bigcount == None or emails > bigcount :
        bigcount = emails
        bigword = words
print bigword, bigcount
