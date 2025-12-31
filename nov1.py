'''
Generate an acronym by taking the first letter of each word in a phrase and returning the uppercase result.

Prompt the user for a phrase or sentence.
Split the phrase into words (ignore blank segments or punctuation).
Collect the first letter of each word, uppercase it, and join into the final acronym.
Handle edge cases such as empty input or single-word phrases gracefully.

'''
while True:
    user_phrase = input('Please enter a phrase or sentence: ')
    #.split() makes the sentence into a list of words
    #word[0] takes first letter in word
    #''.join combines the letters together
    #for word in user_phrase.split() loops, checks for words
    user_acronym = ''.join(word[0].upper() for word in user_phrase.split())
    print(user_acronym)
 