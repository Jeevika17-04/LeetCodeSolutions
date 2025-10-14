class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        n = len(nums)
        sub_len = 1
        firstArr = False
        i = 1

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                sub_len += 1
                
            else:
                if sub_len >= 2 * k or (firstArr and sub_len >= k):
                    return True
                
                firstArr = True if sub_len >= k else False
                sub_len = 1

        return True if sub_len >= 2 * k or (firstArr and sub_len >= k) else False
