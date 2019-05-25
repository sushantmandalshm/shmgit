import math


def sieve(n):
    a_list = [i for i in range(3, n + 1, 2)]
    #return a_list
    #prime_list = []
    for num in a_list:
        for j in range(2,num):
            if num % j == 0:
                a_list.remove(num)
    a_list.insert(0,2)
    return a_list

print(sieve(100))