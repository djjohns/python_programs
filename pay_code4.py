#defines function computepay
def computepay (hours,rate):
    #computes pay based on hours worked and wages
    if hours <= 40:
        pay=(hours*rate)
    else:
        pay= (rate*40)+(rate*1.5*(hours-40))
    print 'your gross pay gor this week is', pay
    return (pay)
#ensures user's input is numerical value
try:
    hours= raw_input('How many hours did you work this period?\n')
    rate= raw_input('What is your current wage per hour?\n')

    hours= float(hours)
    rate= float (rate)
except:
    print 'Please enter a valid number'
    quit()


pay= computepay(hours,rate)


