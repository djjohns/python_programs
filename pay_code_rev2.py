def computepay(hours,rate):
    if fhours>40:
        xhours = (fhours-40)
        xrate = (frate *1.5)
        xpay = (40*frate)+(xhours*xrate)
        print 'Your gross pay for this week is', xpay
    else:
    
        #computs gross pay from given input
        gpay = (frate * fhours)
        #displays gross pay
        print 'Your gross pay for this week is', gpay

#asks user to input hours and rate
rate = raw_input('What is your current wage per hour?\n')
hours = raw_input('How many hours did you work this week?\n')
#insures only nurmic numbers are ran in the program, preventing crash
try:
    # changes input from str to float
    frate = float(rate)
    fhours = float(hours)
    
except:
    print 'Please enter numeric number.'
    quit ()

pay
