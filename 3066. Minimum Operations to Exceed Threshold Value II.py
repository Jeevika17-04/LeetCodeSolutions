import heapq
class Solution(object):
    def minOperations(self, nums, k):
        heapq.heapify(nums)
        count = 0

        while len(nums) > 1 and nums[0] < k:
            heapq.heappush(nums, heapq.heappop(nums) * 2 + heapq.heappop(nums))
            count += 1
        
        return count
