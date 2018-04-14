def three_sum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        j, k = i + 1, len(nums) - 1
        while j < k:
            if nums[j] + nums[k] > -nums[i]:
                k -= 1
            elif nums[j] + nums[k] < -nums[i]:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
                while k - 1 >= 0 and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
    return res
