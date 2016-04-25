
largest = None
smallest = None
while True :
    number = raw_input('Enter a number: ')
    if number == 'done' : break
    try:
        num = int(number)
    except:
        print 'Invalid input'
        continue

    if smallest == None:
        largest = num
        smallest = num
    elif smallest > num:
        smallest = num    
    elif largest < num:
        largest = num       
    
print 'Maximum is',largest
print 'Minimum is',smallest
