res = 0
symbol = 1
if dividend == 0:
    return 0
if divisor == 0:
    return null
if (dividend < 0) ^ (divisor < 0):
    symbol = -1
dividend, divisor = abs(dividend), abs(divisor)
while dividend >= divisor:
    temp = divisor
    i = 1
    while dividend >= temp:
        dividend -= temp
        res += i
        temp *= 2
        i *= 2
res = res * symbol
if symbol < 0:
    return max(res, -2147483648)
else:
    return min(res, 2147483647)