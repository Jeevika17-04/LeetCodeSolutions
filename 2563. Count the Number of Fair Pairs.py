class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        def countLess(summ):
            res = 0
            i = 0
            j = len(nums) - 1
            while i < j:
                while i < j and nums[i] + nums[j] > summ:
                    j -= 1
                res += j - i
                i += 1
            return res

        return countLess(upper) - countLess(lower - 1)
