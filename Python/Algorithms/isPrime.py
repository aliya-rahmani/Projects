# This function receives a number (num), and returns True if the number is prime, and False if it is not prime.
def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(1, int(num / 2)):
        if num % i == 0:
            return False
    return True
