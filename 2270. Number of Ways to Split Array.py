class Solution(object):
    def waysToSplitArray(self, nums):
        right = sum(nums)
        left = result = 0
        n = len(nums)

        for i in range(n - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                result += 1
        return result
