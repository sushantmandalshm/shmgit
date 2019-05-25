from collections import Counter

# even = True if 4 % 2 == 0 else False
# print(even)


# def capitalize_all(t):
#     return [s.capitalize() for s in t]

# print(capitalize_all("Hello"))

# def only_upper(s):
#     return [c for c in s if c.isupper()]

# print(only_upper("Hello"))

# count = Counter("Hello")
# print(count)


def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

print(is_anagram("Mom", "Mom"))