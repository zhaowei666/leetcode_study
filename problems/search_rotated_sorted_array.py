# unfinished

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = int((left + right) / 2)
        print(mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            if nums[left] < target:
                left += mid + 1
            elif nums[left] > target:
                right = mid - 1
            else:
                return left
        else:
            if nums[left] > target:
                left = mid + 1
            elif nums[left] < target:
                right = mid - 1
            else:
                return left
        print(left, right)
    return -1


a = [4,5,6,7,0,1,2]
b= [1,3]
print(search(b, 3))