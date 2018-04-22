def combination_sum(candidates, target):
    candidates.sort()
    res = []

    def recursive(k, path, residue):
        if residue == 0:
            if path and path not in res:
                res.append(path)
        else:
            for i in range(k, len(candidates)):
                if candidates[i] > residue:
                    continue
                else:
                    recursive(i, path + [candidates[i]], residue - candidates[i])
        return

    recursive(0, [], target)
    return res
