grade = raw_input('What was the score?\n')
try:
    grade = float(grade)
    if grade >= (0.9):print 'Your score was an A'
        
    elif grade < (0.9) and grade >= (0.8):print 'Your score was a B'
        
    elif grade < (0.8) and grade >=(0.7):print 'Your score was a C'
        
    elif grade < (0.7) and grade >= (0.6):print 'Your score was a D'
        
    elif grade < (0.6):print 'Your score was a F'
        
except:
    print 'Please enter a valid grade.'
