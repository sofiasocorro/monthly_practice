'''
Generate an acronym by taking the first letter of each word in a phrase and returning the uppercase result.

Prompt the user for a phrase or sentence.
Split the phrase into words (ignore blank segments or punctuation).
Collect the first letter of each word, uppercase it, and join into the final acronym.
Handle edge cases such as empty input or single-word phrases gracefully.

'''
while True:
    user_phrase = input('Please enter a phrase or sentence: ')
    #revised_input= user_phrase.replace (' ', '').upper().split()
    d = ''.join(word[0].upper() for word in user_phrase.split())
    print(d)