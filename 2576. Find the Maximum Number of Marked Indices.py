class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        n = len(nums)
        nums.sort()
        i, j = 0, n // 2
        marked = 0

        while i < n // 2 and j < n:
            if nums[i] * 2 <= nums[j]:
                marked += 2
                i += 1
            j += 1
        
        return marked
