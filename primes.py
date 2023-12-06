"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes(number_of_primes):
    """Return a list of the first number_of_primes prime numbers."""
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be a positive integer")

    prime_list = []
    num = 2  # Start checking for prime from 2
    while len(prime_list) < number_of_primes:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list