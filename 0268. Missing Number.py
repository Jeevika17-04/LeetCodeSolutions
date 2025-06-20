class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        xor = n

        for ind in range(n):
            xor = xor ^ ind ^ nums[ind]
        
        return xor
