def isPalindrome(n):
    if n < 0:
        return False
    else:
        num_str = str(n)
        if num_str[::-1] == str(n):
            return True
        else:
            return False

print(isPalindrome(12121))
print(isPalindrome(2147447412))