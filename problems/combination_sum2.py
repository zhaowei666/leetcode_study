def combination_sum(candidates, target):
    res = []

    def recursive(k, path, residue):
        if residue == 0 and path and path not in res:
            res.append(path)
        else:
            for i in range(k + 1, len(candidates)):
                if residue < candidates[i]:
                    return
                else:
                    recursive(i, path + [candidates[i]], residue - candidates[i])

    candidates.sort()
    recursive(-1, [], target)
    return res
