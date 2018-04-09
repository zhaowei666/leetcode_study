class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        nums.sort()
        for idx, num in enumerate(nums):
            if target - num in dic:
                return [idx, dic[target - num]]
            else:
                dic[num] = idx

