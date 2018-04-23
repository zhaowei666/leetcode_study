res = []
candidates.sort()


def backtrack(path, remain, k):
    if remain == 0:
        if path not in res:
            res.append(path)
    for i in range(k, len(candidates)):
        if remain < candidates[i]:
            break
        if i > k and candidates[i] == candidates[i - 1]:
            continue
        else:
            backtrack(path + [candidates[i]], remain - candidates[i], i + 1)
    return


backtrack([], target, 0)
return res