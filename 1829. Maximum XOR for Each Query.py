class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        mx = (1 << maximumBit) - 1
        ans = []
        xors = 0

        for num in nums:
            xors ^= num
            ans.append(xors ^ mx)

        return ans[::-1]
