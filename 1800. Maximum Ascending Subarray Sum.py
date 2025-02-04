class Solution(object):
    def maxAscendingSum(self, nums):
        n = len(nums)
        curr_sum = total = nums[0]
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                curr_sum += nums[i + 1]
            else :
                curr_sum = nums[i + 1]
            total = max(curr_sum, total, nums[i])

        return total
