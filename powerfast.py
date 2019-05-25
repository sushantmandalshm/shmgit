def powerfast(base, power):
    if power == 0:
        return 1
    else:
        partial = powerfast(base, power // 2)
        result = partial * partial
        if power % 2 == 1:
            result *= base
        return result


print(powerfast(2, 5))
