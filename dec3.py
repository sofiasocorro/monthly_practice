'''
---------------- Prime Number Tester ---------------------------
Given N, report whether N is prime and list all primes up to N; handle invalid/edge inputs cleanly.

Prompt for integer N; validate (integer, N ≥ 0).
Write a function to test primality (trial division up to √N).
Print whether N is prime; then generate and print all primes ≤ N.
Handle edge cases (N < 2 → no primes).
Examples

Input: N = 10
Output: "10 is not prime" and "Primes up to 10: 2, 3, 5, 7"
Correct detection and list.
not_prime = print(f'{user_input} is not prime')
prime_numb = print(f'Primes up  to {user_input}: )

'''
while True:
    user_input = float(input('\nPlease type integer N = '))

    if (user_input >= 0 or user_input == 0):
        print(user_input)