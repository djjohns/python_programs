largest=None
smallest=None
while True:
    number= raw_input("Enter a number:")
    if number == "done": break
    try:    
        n=int(number)
    except: 
        print "Enter a valid number" 
        continue
    if smallest is None or n<smallest:
        smallest=n
    elif n>largest:
        largest=n
print "Maximum is", largest
print "Minimum is", smallest
