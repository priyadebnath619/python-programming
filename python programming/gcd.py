import math

# Take input from the user
numbers = list(map(int, input("Enter two or more integers separated by spaces: ").split()))

# Find GCD of all numbers
gcd_result = numbers[0]
for n in numbers[1:]:
    gcd_result = math.gcd(gcd_result, n)

print("The greatest common divisor (GCD) is:", gcd_result)