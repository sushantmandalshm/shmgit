s = 'abcbcd'
current = s[0]
maxLen = 0
longest = s[0]
for i in range(len(s)-1):
    if s[i+1] >= s[i]:
        current += s[i+1]
        if len(current) > maxLen:
                maxLen = len(current)
                longest = current
    else:
        current = s[i+1]
print('Longest substring in alphabetical order is: ',longest)
