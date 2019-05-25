def decimalToBinary(n):
    a_list = []
    binary = ''
    while n > 0:
        rem = n % 2
        a_list.append(rem)
        n = n // 2
    a_list.reverse()
    for num in a_list:
        binary = binary + str(num)
    return int(binary)

print(decimalToBinary(15))