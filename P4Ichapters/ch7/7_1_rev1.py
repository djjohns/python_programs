#asks for user input and assigns file name to fname
fname = raw_input('Enter a file name: ')
#shortcuts to open common file upon hitting enter
if len(fname) == 0:
    fname = 'mbox-short.txt'
#opens file    
fhand = open (fname)
#starts count and total 
count = 0.0
total = 0.0
#Starts loop to find data starting with a specific paramater
for line in fhand :
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:') :
    count = count+1
    float(count)
    float (total)
    data = line[20:]
    num = float(data)
    total = total + num
#averages number of times specified data appears within file
average = total/count
#returns the average to user
print 'Average spam confidence: ',average
        
