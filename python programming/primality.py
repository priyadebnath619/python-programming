# Problem: Primality Test
# Given an integer, determine if it is a prime number

# Input from user
num =int(input("Enter a number: "))

# Handle special cases
if num <= 1:
    print("Not a prime number")
else:
    # Assume it is prime unless proven otherwise
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # Output result
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")