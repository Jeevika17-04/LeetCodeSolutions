from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        n = len(nums)
        freq = defaultdict(int)
        buckets = [[] for i in range(n + 1)]
        res = []

        for key in nums:
            freq[key] = freq[key] + 1
        
        for key, val in freq.items():
            buckets[val].append(key)

        for i in range(n, 0, -1):
            if k > 0:
                for j in buckets[i]:
                    if k > 0:
                        res.append(j) 
                        k -= 1
                    else:
                        break
            else:
                break
            
        return res
