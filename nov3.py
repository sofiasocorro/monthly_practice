'''
--------------------- LONGEST WORD IN A SENTENCE ---------------------

Analyze a sentence and return the first longest word that appears.

Accept a sentence or phrase as input.
Normalize punctuation so words can be compared consistently.
Track the longest word length; if there is a tie, keep the first occurrence.
Return or print the longest word (optionally include its length).
Examples

Input: "Coding is both fun and challenging"
Output: "challenging"
The longest word has 11 characters and appears once.

'''
while True:
    user_sent = input('Please enter a sentence or phrase: ').split()
    long_word = max(user_sent, key = len)
    print(f'The longest word is {long_word}')