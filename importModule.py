# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:16:26 2018

@author: CyberCloned
"""

# =============================================================================
# import random
# import math
# 
# for i in range(10):
#     print(rand.randrange(100, 250), random.randint(100, 250), random.randint(100, 250))
#     
# print(math.pi)
# =============================================================================

import random
number = random.randint(1, 25)
number_of_guesses = 0
while number_of_guesses < 15:
    print('Guess a number between 1 and 25:')
    guess = input()
    guess = int(guess)
    number_of_guesses = number_of_guesses + 1
    if guess == number:
        print("You just got the number!")
        print(number_of_guesses)
        break
