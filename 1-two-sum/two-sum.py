class Solution:
    def twoSum(self, nums, target):
        d = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], i]
            d[num] = i