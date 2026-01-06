'''
----------------ROCK, PAPER, SCISSORS --------------------------------

Play a single round of Rock, Paper, Scissors against a random computer opponent.

Randomly select Rock, Paper, or Scissors for the computer.
Prompt the user for their choice and validate the input.
Compare selections to determine win, lose, or draw and print a descriptive message.
Always display both choices so the user understands the result.
Examples

Input: user_choice=Rock, computer_choice=Scissors
Output: "You chose Rock, and the computer chose Scissors. You win!"
Rock beats Scissors, so the user wins.
'''

import random
choices = ['rock', 'paper', 'scissors']

while True:
    computer_choice = random.choice(choices)
    user_choice = input('\nPlease select Rock, Paper, or Scissors: ').lower()

    if user_choice == computer_choice:
        print(f'\nYou both choose {user_choice}. There was a tie!')

    elif user_choice == 'rock' and computer_choice == 'scissors' or user_choice == 'scissors' and computer_choice == 'paper' or user_choice == 'scissors' and computer_choice == 'paper':
        print(f'\nYou chose {user_choice}, and the computer chose {computer_choice}. You win!')

    else:
        print(f'\nYou chose {user_choice}, and the computer chose {computer_choice}. Computer win!')
  