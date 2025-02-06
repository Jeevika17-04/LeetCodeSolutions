from collections import defaultdict
class Solution(object):
    def tupleSameProduct(self, nums):
        freq = defaultdict(int)
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                freq[nums[i] * nums[j]] += 1

        for key, value in freq.items():
            if value > 1:
                count += (value * (value - 1)) // 2 
        
        return count * 8
