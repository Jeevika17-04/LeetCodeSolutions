from collections import defaultdict
class Solution(object):
    def maxFrequencyElements(self, nums):
        d = defaultdict(int)

        for i in nums:
            d[i] = d[i] + 1

        max_elements = 0
        max_freq = 0

        for key, value in d.items():
            if d[key] > max_freq:
                max_elements = d[key]
                max_freq = d[key]
            elif d[key] == max_freq:
                max_elements += d[key]
        
        return max_elements
