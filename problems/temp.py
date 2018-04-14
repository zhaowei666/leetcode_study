nums.sort()
res = sum(nums[0: 3])
n = len(nums)
for i in range(n - 2):
    if i > 1 and nums[i] == nums[i - 1]:
        continue
    left, right = i + 1, n - 1
    while left < right:
        s = nums[i] + nums[left] + nums[right]
        if s == target:
            return s
        if abs(s - target) < abs(res - target):
            res = s
        if s > target:
            right -= 1
        elif s < target:
            left += 1
        else:
            left += 1
            right -= 1
return res

