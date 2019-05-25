def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)
    return S 

print(reverse([1,2,3,4,5],0,5))