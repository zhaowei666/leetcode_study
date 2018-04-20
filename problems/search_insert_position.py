def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = int((left + right) / 2)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            print(left, right)
            return mid
    print(left, right)
    return left

a = [1, 2, 5, 6]
print(search_insert(a, 4))