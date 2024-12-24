class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        zeros = []
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            if nums[i] == 0:
                zeros.append(i)
            if len(zeros) >= 2:
                return [0] * n
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[n - i - 1] = suffix[n - i] * nums[n - i]
        
        if len(zeros) == 1:
            i = zeros[0]
            return [0] * i + [prefix[i] * suffix[i]] + [0] * (n - i - 1)

        for i in range(n):
            nums[i] = prefix[i] * suffix[i]
        return nums
