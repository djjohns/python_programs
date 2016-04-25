#imports the Regular Expression library to us in this program
import re
sum=0
NumExtracted =0
#prompts user for file name and stores it as 'name'
name = raw_input('PLease enter file name:')

#Shortcuts user to file: regex_sum_42.txt upon pressing enter
if len(name) < 1 : name = 'regex_sum_42.txt'

#Try and except insurance to user does not enter invalid file name
try:
    fh = open(name)
except:
    print 'File cound not be opened: ',name
    exit()
    
#Start variable NumList to be summed later
NumList=list()
#For loop to extract all numbers in the file and compute the sum
#and number of digits extracted then prints the results
for line in fh:
    ExtractedNum=re.findall('[0-9]+',line)
    if len(ExtractedNum) >0:
        NumExtracted += len(ExtractedNum)
        NumList=NumList+ExtractedNum

for Num in NumList:
    sum=sum + int(Num)
print 'The Sum of the digits extracted from the file is: '
print sum
print 'The Number of digits extracted are: '
print NumExtracted
