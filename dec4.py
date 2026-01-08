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