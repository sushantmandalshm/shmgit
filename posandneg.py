def pos(n):
    #a = [i for i in range(n-1, -1, -1)]
    for num in [i for i in range(n-1, -1, -1)]:
        print(num, end=" ")

def neg(n):
    for num in [i for i in range(n, 1, 1)]:
        print(num, end=" ")


# pos(4)
#neg(-3)