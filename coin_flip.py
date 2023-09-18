# Jack Carruthers
# Coin flip 

import random # import library for random
print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
input()
flips = 0
heads = 0
tails = 0 # setting start values
end = ("\n") # variable for line space
while flips < 1000: 
    if random.randint(0, 1) == 1:
        heads = heads + 1
        tails = tails + 1 
    flips = flips + 1  # while loop, whilst flips are under 10000 it will increase continously.

    if flips == 900: # defines when flips reach 900 
        print('900 flips and there have been ' + str(heads) + ' heads.\n Tails came up', str(tails), 'times.')
        print(end) # prints space
        
    if flips == 100: # defines when flips reach 100
        print('At 100 tosses, heads has come up ' + str(heads) + ' times so far.\n Tails came up', str(tails),'times.')
        print(end) # prints space 
        
    if flips == 500: # defines when flips reach 500 
        print('Halfway done, and heads has come up ' + str(heads) + ' times. \n Tails occured', str(tails), 'times')
        print(end) # prints space


quest = input("Would you like to guess the final number of heads? (yes) (no)\n") # question to either start or dont
if quest == ("yes"):
    guess = int(input(" Enter a value between 0 and 1000 \n"))
    if heads-10 <= guess <= heads+10: # if guess is within 10 of the value 
        print("Confirmed, You was close!")
        print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times! \n Throughout, tails occured', str(tails), 'times')

    else: # if anything other than the range of ten of answer 
        print("Sorry, you was not close.")
        print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times! \n Throughout, tails occured', str(tails), 'times')
        
elif quest == ("no"): # if no is inputted
    print("Alright, the final answer was", str(heads), "times")
else:
    print("Invalid, answer yes or no") # if anything else than yes or no entered it allows user to try again

    


    


        
