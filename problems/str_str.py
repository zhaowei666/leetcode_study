def str_str(haystack, needle):
    m, n = len(haystack), len(needle)
    for i in range(m - n + 1):
        if needle == haystack[i: i + n]:
            return i
    return -1

a = ''
b = ''
print(str_str(a, b))