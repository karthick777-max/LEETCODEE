class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        freq = {0: 1}   # prefix sum 0 seen once

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]

            if prefix_sum in freq:
                freq[prefix_sum] += 1
            else:
                freq[prefix_sum] = 1

        return count
        