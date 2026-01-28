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


while True:
    digits = ['0','1','2','3','4','5','6','7','8','9']
    #random.sample for unique digits
    #''.join makes characters to a string
    secret_code = ''.join(random.sample(digits,4))
    print(secret_code)


    attempts = 5
    user_input = str(input('Guess = '))

    if user_input == secret_code:
        print('Bulls: 4, You won!')
        break

    if len(secret_code) == len(user_input) and :
        print('yes')