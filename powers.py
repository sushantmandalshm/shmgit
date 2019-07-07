def printIncreasingPower(x):
    power = 1
    while power**2 <= x:
        print(power**2, end = " ")
        power += 1

printIncreasingPower(100)