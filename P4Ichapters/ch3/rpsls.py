import random

# helper functions

def number_to_name(num):
    if num == 0:
        return 'rock'
    elif num == 1:
        return 'Spock'
    elif num == 2:
        return 'paper'
    elif num == 3:
        return 'lizard'
    else:
        return 'scissors'

    
def name_to_number(name):
   
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    else:
        return 4
    
# main function

def rpsls(guess):
    
    # convert name to player_number using name_to_number
    
    player_number = name_to_number(guess)
    
    # compute random guess for comp_number using random.randrange()
    
    comp_number = random.randrange(0,5)
    
    # convert comp_number to name using number_to_name
    
    computer_guess = number_to_name(comp_number) 
    
    # compute difference of player_number and comp_number modulo five
    
    result = (player_number - comp_number) % 5
    
    

# use if/elif/else to determine winner    

    if result == 1 or result == 2:
        winner = 'Player wins!'
    elif result == 3 or result == 4:
        winner = 'Computer wins!'
    else:
        winner = 'Player and Computer tie!'

        
# print results

    print
    print 'Player chooses', guess
    print 'Computer chooses', computer_guess
    print winner

    
# test your code
#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")
