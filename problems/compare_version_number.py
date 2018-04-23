def compare(version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    m, n = len(v1), len(v2)
    for i in range(min(m, n)):
        if int(v1[i]) < int(v2[i]):
            return -1
        elif int(v1[i]) > int(v2[i]):
            return 1
    if m > n and sum([int(x) for x in v1[n: m]]):
        return 1
    elif m < n and sum([int(x) for x in v2[m: n]]):
        return -1
    return 0


print(compare("1.0", "1"))