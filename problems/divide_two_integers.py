def divide(dividend, divisor):
    if divisor == 0:
        return 0
    if dividend == 0:
        return 0
    if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0):
        symbol = 1
    else:
        symbol = -1
    res = 0
    dividend, divisor = abs(dividend), abs(divisor)
    while dividend >= divisor:
        temp = divisor
        temp2 = 1
        while dividend >= temp:
            dividend -= temp
            res += temp2
            temp += temp
            temp2 += temp2
    res = res * symbol
    if symbol < 0:
        return max(res, -2147483648)
    else:
        return min(res, 2147483647)


print(divide(10, 3))
