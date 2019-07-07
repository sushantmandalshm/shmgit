def counting(a_str, part_string):
    count = 0
    a_len = len(a_str) - 2
    for i in range(a_len):
        if a_str[i] + a_str[i+1] + a_str[i+2] == part_string:
            count += 1
    return count


print(counting("azcbobobegghakl","bob"))