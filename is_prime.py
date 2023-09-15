# Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
# NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python/65046975fc50b5048207cd8e

import math

def is_prime(num):
    if num == 2:
        return True
    if num == 0 or num == 1 or num < 0:
        return False
    nums_below_sqrt = list(range(2, math.trunc(math.sqrt(num) + 1)))
    for int in nums_below_sqrt:
        if num % int == 0:
            return False
    return True

print("Should be False")
print(is_prime(1))
print("Should be True")
print(is_prime(2))
print("Should be False")
print(is_prime(1))
print("Should be False")
print(is_prime(20000))
print("Should be True")
print(is_prime(5099))
