#asks user to input hours and rate
rate = raw_input('What is your current wage per hour?\n')
frate = float(rate)
hours = raw_input('How many hours did you work this week?\n')
fhours = float(hours)
if hours>40:
        xhours = (fhours-40)
        xrate = (frate *1.5)
        xpay = (40*frate)+(xhours*xrate)
        print 'Your gross pay for this week is', xpay
else:
    
    #computs gross pay from given input
    gpay = (frate * fhours)
    #displays gross pay
    print 'Your gross pay for this week is', gpay
