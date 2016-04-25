

import re
sample = open ('regex_sum_173650.txt')
total =0
dignum = 0 

for line in sample:
    line = line.rstrip()
    dig= re.findall('[0-9]+', line)

    if len(dig) >0:
        dignum += len(dig)
        linetotal= sum(map(int, dig))
        total += linetotal

print 'The number of digits are:  ' 
print dignum
print 'The sum is: '
print total     
print 'The sum ends with: '
print  total % 1000

