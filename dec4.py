'''
----------------- Codebreaker (Bulls & Cows) --------------

Computer picks a random 4-digit code (no repeats). After each 4-digit guess, print Bulls (right digit, right place) and Cows (right digit, wrong place) with limited attempts and input checks.

Randomly generate a 4-digit secret with no repeated digits.
Validate guesses: exactly 4 digits, all unique; re-prompt on invalid input.
After each valid guess, compute and display Bulls/Cows; track remaining attempts.
End with win (all Bulls) or loss (reveal secret).
Examples

Input: Secret = 4279, Guess = 4972
Output: "Bulls: 1, Cows: 2"
4 is a Bull; 9 and 7 (or 2 and 7) are Cows depending on positions.

'''

import random

digits = list('0123456789')    
#random.sample for unique digits
#''.join makes characters to a string
#(digits,4) picks up 4 digits
secret_code = ''.join(random.sample(digits,4))

max_attempts = 5
remaining_attempts = max_attempts

#loops game while the user still has attempts
while remaining_attempts > 0:
    user_input = input(f'Attempts: {remaining_attempts}, Guess = ')

    #.isdigit() checks if its numbers
    if not user_input.isdigit():
        print('Please only use digits')
        continue
    
    #checks if user input is less or greater than 4 digits
    if len(user_input) != 4:
        print('Enter only 4 digits')
        continue

    #set(user_input) checks if there's duplicates and if there is, it removes it
    #if the length changes after set(user_input) then there was duplicates
    if len(set(user_input)) != 4:
        print('Digits cannot repeat.')
        continue


    bulls = 0
    cows = 0

    for word in range(4):
        #checks if the it has the same digit and position
        if user_input[word] == secret_code[word]:
            bulls += 1
        #checks if digit is in the secret code, but its not in the same position
        elif user_input[word] in secret_code:
            cows +=1

    print(f'Bulls: {bulls}, Cows: {cows}')

    if bulls == 4:
        print('You win!')
        break

    remaining_attempts -= 1

if remaining_attempts == 0:
    print(f'Attempts: {remaining_attempts}, The secret code was {secret_code}')

   
