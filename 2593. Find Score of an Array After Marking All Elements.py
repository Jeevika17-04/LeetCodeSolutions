class Solution(object):
    def findScore(self, nums):
        n = len(nums)
        indices_sorted = sorted(range(n), key = lambda i: nums[i])
        score = 0
        marked = [False] * n

        for i in indices_sorted:
            if marked[i]:
                continue

            if i > 0:
                marked[i - 1] = True
            if i < n - 1:
                marked[i + 1] = True

            marked[i] = True
            score += nums[i]
            
        return score
