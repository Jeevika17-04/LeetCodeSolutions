class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        temp = [None] * (k)
        for i in range(k):
            temp[i] = nums[-k + i]
        for i in range(n - 1, k-1, -1):
            nums[i] = nums[i - k]
        for i in range(k):
            nums[i] = temp[i]
