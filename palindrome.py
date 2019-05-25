def isPalindrome(n):
    if n < 0:
        return 0
    else:
        num_str = str(n)
        if num_str[::-1] == str(n):
            return 1
        else:
            return 0

print(isPalindrome(12121))
print(isPalindrome(2147447412))