class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        maxSum = nums[0]
        maxEnding = nums[0]

        for i in range(1, n):
            maxEnding += nums[i]
            if maxEnding < nums[i]:
                maxEnding = nums[i]
            
            if maxSum < maxEnding:
                maxSum = maxEnding
        
        return maxSum
