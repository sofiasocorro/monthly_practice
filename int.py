vowels= ['a','e','i','o','u']

while True:
	user_input = input('Enter a word: ').lower()
    count_vowels = 0
	for letter in user_input:       
            if letter in vowels:
                    count_vowels += 1
                    print(f'Vowel count: {count_vowels}')
                    break