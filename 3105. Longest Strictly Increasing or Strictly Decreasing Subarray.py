class Solution(object):
    def longestMonotonicSubarray(self, nums):
        decreasing = False
        increasing = False
        count = curr = 1
        n = len(nums)

        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                if not increasing:
                    increasing = True
                    decreasing = False
                    count = max(curr, count)
                    curr = 1
                curr += 1
            elif nums[i] > nums[i + 1]:
                if not decreasing:
                    decreasing = True
                    increasing = False
                    count = max(curr, count)
                    curr = 1
                curr += 1
            else:
                decreasing = False
                increasing = False
        return max(curr, count)
