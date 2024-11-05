class Solution(object):
    def twoSum(self, nums, target):
        ans=[]
        count=len(nums)
        for i in range(count):
            x=target-nums[i]
            if (x) in nums[i+1:]:
                ans+=[i,x]
                continue
            n=len(ans)
            if n!=0 and ans[1]==nums[i]:
                ans[1]=i
                break
        return ans
