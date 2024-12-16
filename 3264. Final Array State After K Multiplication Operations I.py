class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        i = 0
        n = len(nums)
        for i in range(k):
            ind = 0
            for j in range(n):
                if nums[j] < nums[ind]:
                    ind = j
            nums[ind] *= multiplier

        return nums
