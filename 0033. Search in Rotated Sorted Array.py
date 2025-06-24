class Solution(object):
    def search(self, nums, target):
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[lo]:
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            else:
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                
                else:
                    hi = mid - 1

        return -1
