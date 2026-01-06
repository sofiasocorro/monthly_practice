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
