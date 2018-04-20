def count_and_say(n):
    if n <= 0:
        return ''
    res = '1'
    for i in range(1, n):
        count, digit = 1, res[0]
        current = ''
        for j in range(1, len(res)):
            if res[j] == res[j - 1]:
                count += 1
            else:
                current += str(count) + str(digit)
                digit = res[j]
                count = 1
        current += str(count) + str(digit)
        res = current
    return res

