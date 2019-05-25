import math


def isPrime(n):
    n = abs(n)
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return 0
    else:
        for i in range(3, int(math.sqrt(n) + 1),2):
            if n % i == 0:
                return 0
        return 1

print(isPrime(37))