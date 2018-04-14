def three_sum_cloest(nums, target):
    if len(nums) < 3:
        return 0
    res = sum(nums[0: 3])
    nums.sort()
    for i in range(len(nums)):
        j, k = i + 1, len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if abs(s - target) < abs(res - target):
                res = s
            if s > target:
                k -= 1
            elif s < target:
                j += 1
            else:
                return res
    return res

