import math

def allFactors(n):
    a_list = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            a_list.append(i)
            if i != math.sqrt(n):
                a_list.append(n//i)

    return sorted(a_list)


print(allFactors(36))