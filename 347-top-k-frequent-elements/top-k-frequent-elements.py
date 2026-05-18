class Solution:
    def topKFrequent(self, nums, k):

        freq = {}

        # Count frequency
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in freq:
            count = freq[num]
            buckets[count].append(num)

        result = []

        # Traverse from highest frequency
        for i in range(len(buckets) - 1, 0, -1):

            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result
                    