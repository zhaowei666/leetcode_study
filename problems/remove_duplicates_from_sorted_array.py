def remove_duplicates(nums):
    n = 0
    if len(nums) < 2:
        return len(nums) - 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        n += 1
        nums[n] = nums[i]
    return n + 1