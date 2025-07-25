class Solution(object):
    def maxSum(self, nums):
        max_element = -100
        max_sum = 0
        counter = [0] * 101

        for num in nums:
            if num > 0 and counter[num] != 1:
                max_sum += num
                counter[num] = 1
            elif num > max_element:
                max_element = num
        
        return max_element if max_sum == 0 else max_sum 
