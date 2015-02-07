#prompts user for celsius temp.
celsius = raw_input('enter temp.reading in c*.\n')
#converts input from str to float
fcels = float(celsius)
#converts celsius temp to fahrenheit
fahrenheit = (fcels+32)
#displays temp conversion for user
print ('Your fahrenheit temp. would be'), fahrenheit
