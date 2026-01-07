'''
----------------------ANAGRAM CHECKER -----------------------   
Compare two input strings and report if they're anagrams, ignoring spaces, punctuation, and case; include basic input validation.

Prompt for two input strings.
Normalize: remove non-alphanumeric chars and lowercase both strings.
Compare by counting characters (e.g., dict/Counter) or sorting; output “anagrams” or “not anagrams.”
Handle edge cases (empty inputs, only punctuation, different normalized lengths).
Examples

Input: "Listen" and "Silent"
Output: "The strings are anagrams."
After normalization, letter counts match.

'''



while True:
    word_one = input('Please type first: ').lower()
    word_two = input('Please type second word: ').lower()

    if len(word_one) == len(word_two) and sorted(word_one) == sorted(word_two):
        print('\nThe strings are anagrams\n')
    
    else:
        print('\nThe strings are not anagrams\n')
    


