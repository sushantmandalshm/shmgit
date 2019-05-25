def linear_sum(a_list,n):
    if n == 0:
        return 0
    else:
        return linear_sum(a_list, n - 1) + a_list[n - 1]

a_list = [1, 2, 3, 4, 5]
n = len(a_list)
print(linear_sum(a_list,n))