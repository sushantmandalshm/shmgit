def numsetbits(n):
    count = 0
    bits = '{:032b}'.format(n)
    for bit in bits:
        if bit == '1':
            count += 1
    return count


print(numsetbits(50))