def primesum(n):
    a_list = []
    #dual = []
    for i in range(n):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                a_list.append(i)
    #print(a_list)
    for num in a_list:
        if n - num in a_list:
            #dual.append(n-num)
            return num, n - num
    #dual.sort()
    #return dual
    #return dual[0], dual[1]

print(primesum(1048574))
print(primesum(4))
