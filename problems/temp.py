        candidates.sort()
        if not candidates:
            return []
        res = []

        def backtrack(path, residue, k):
            if residue == 0:
                if path not in res:
                    res.append(path)
                return
            for i in range(k, len(candidates)):
                if residue < candidates[i]:
                    break
                if i > k and candidates[i] == candidates[i - 1]:
                    continue
                else:
                    backtrack(path + [candidates[i]], residue - candidates[i], i)
            return

        backtrack([], target, 0)
        return res