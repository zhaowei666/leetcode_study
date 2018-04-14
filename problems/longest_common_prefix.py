def longest_common_prefix(strs):
    if not strs:
        return ''
    prefix = strs[0]
    for s in strs:
        while prefix:
            if prefix == s[0: len(prefix)]:
                break
            else:
                prefix = prefix[0: -1]
        if not prefix:
            return ''
    return prefix