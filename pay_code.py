#asks user to input hours and rate
rate = raw_input('What is your current wage per hour?\n')
hours = raw_input('How many hours did you work this week?\n')
#converts str to float
frate = float(rate)
fhours = float(hours)
#computs gross pay from given input
gpay = (frate * fhours)
#displays gross pay
print 'Your gross pay for this week is', gpay
