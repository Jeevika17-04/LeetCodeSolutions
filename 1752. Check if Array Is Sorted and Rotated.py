class Solution(object):
    def check(self, nums):
        flag = False
        n = len(nums) 
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if flag:
                    return False
                flag = True

        if not flag:
            return True
            
        return True if nums[0] >= nums[-1] and flag else False
