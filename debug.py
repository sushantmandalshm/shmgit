def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)


def f(n):
    """
    n: integer, n >= 0.
    """
    if n == 0:
        return 1
    else:
        return n * f(n-1)


def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")


def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0


def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers


print(normalize([0, 0, 0]))
