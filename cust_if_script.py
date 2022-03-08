#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'You are '

# wrap connection in a float() to accept decimals as numbers
number = float(input("Please choose a number from 1-3: "))

# if input value was higher or equal to 25
if number == 1:
    message = message + 'the GOAT, Michael Jordan!'
elif number == 2:
    message = message + 'not the GOAT, but you are Kobe Bryant!'
elif number == 3:
    message = message + '..oh.. you are just Lebron James.'
else:
    message = 'Sorry, this is only a top 3 list...'
print(message)
