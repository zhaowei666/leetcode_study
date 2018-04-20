def say(k):
    if k == 1:
        return '1'
    else:
        s = say(k - 1)
        t = len(str(s))
        temp = s[0]
        Ntemp = 1
        result = ''
        for i in range(1, t):
            if temp == s[i]:
                Ntemp += 1
            elif temp != s[i]:
                result += str(Ntemp) + temp
                Ntemp = 1
                temp = s[i]
        result += str(Ntemp) + temp
    return result


return say(n)