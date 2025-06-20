class Solution(object):
    def firstMissingPositive(self, nums):
        nums.sort()
        curr = 0
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] <= 0:
                i += 1
            elif nums[i] == curr or nums[i] == curr + 1:
                curr = nums[i]
                i += 1
            else:
                return curr + 1
                
        return curr + 1
