# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers.
# Then using modulo arithmetic, the winners of the rock paper scissors lizard spock game can be easily calculated.  
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# this order is significant, as each element beats the two in front of it, and loses to the two before it.

def name_to_number(name): 
    # convert name to number using if/elif/else    
    if name == 'rock':
        name = 0
    elif name == 'Spock':
        name = 1
    elif name == 'paper':
        name = 2
    elif name == 'lizard':
        name = 3
    elif name == 'scissors':
        name = 4
    else:
        print "Sorry, that isn't one of the choices"
    return name

def number_to_name(number):
    # convert number to a name using if/elif/else
    if number == 0:
        number = 'rock'
    elif number == 1:
        number = 'Spock'
    elif number == 2:
        number = 'paper'
    elif number == 3:
        number = 'lizard'
    elif number == 4:
        number = 'scissors'
    else:
        print "That isn't one of the choices."
    return number

def rpsls(player_choice): 
    import random
    print "\n"
    
    # print out the message for the player's choice
    print "You have chosen: " + player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "The computer randomly chose: " + comp_choice
    
    # use modulo arithmetic to determine the winner. We compute the difference of comp_number and player_number modulo five
    calculation = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if (calculation == 1) or (calculation == 2):
        print "Hooray, you are the winner!"
    elif (calculation == 3) or (calculation == 4):
        print "Uh oh, the computer wins."
    elif calculation == 0:
        print "It's a tie."
    
# run the game 5 times, each with a different choice.
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
