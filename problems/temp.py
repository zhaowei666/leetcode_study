m, n = len(haystack), len(needle)
if n == 0:
    return 0
for i in range(m - n + 1):
    if needle == haystack[i: i + n]:
        return i
return -1
