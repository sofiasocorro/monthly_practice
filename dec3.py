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
    user_input = int(input('\nPlease type an integer N = '))

    if user_input <0:
        print('Please a positive integer.')
        continue
    
    true_prime = True

    if user_input <2:
        true_prime = False

    
    else:
        for i in range(2, int(user_input**0.5) + 1):
            if user_input%i == 0:
                true_prime = False
                break

    if true_prime:
        print(f'{user_input} is prime')

    else:
        print(f'{user_input} is not prime')

    
    primes = []
    
    for num in range(2, user_input + 1):
        prime = True
        for i in range(2, int(num**0.5)+1):
            if num%1 == 0:
                prime = False
                break
        
        if prime:
            primes.append(str(num))
    
    if primes:
        print(f'Primes up to {user_input}: {', '. join(primes)}')

    else:
        print(f'Primes up to {user_input}: None')

'''          
    for i in range(2, user_input):
        if user_input%i==0:
            print(f'{user_input} is not a prime')

            primes = []
            for num in range(2, user_input + 1):
                primes.append(str(num))
            print(f'Primes up to {user_input}: {', '.join(primes)}')
            break

'''   
