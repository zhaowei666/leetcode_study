def letterCombinations(digits):
    letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def recursive_combinations(s, n, res=[]):
        if n == len(digits):
            if s:
                res.append(s)
        else:
            for l in letters[int(digits[n])]:
                recursive_combinations(s + l, n + 1)
        return res

    return recursive_combinations('', 0)
