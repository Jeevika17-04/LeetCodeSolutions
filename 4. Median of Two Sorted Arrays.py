class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        mid = []
        if (n + m ) % 2 == 1:
            mid = [((n+m)//2) + 1]
        else :
            mid = [((n+m)//2), ((n+m)//2) + 1]
        ind = 0 
        i = j = 0
        curr = 0
        tot =  0
        while i < n and j < m:
            print(tot)
            if nums1[i] < nums2[j]:
                ind += 1
                curr = nums1[i]
                i += 1
            else:
                ind += 1
                curr = nums2[j]
                j += 1
            if mid[-1] == ind:
                tot += curr
                break
            elif mid[0] == ind :
                tot += curr
        while i < n :
            ind += 1
            curr = nums1[i]
            i += 1
            if mid[-1] == ind:
                tot += curr
                break
            elif mid[0] == ind :
                tot += curr
        while j < m :
            ind += 1
            curr = nums2[j]
            j += 1
            if mid[-1] == ind:
                tot += curr
                break
            elif mid[0] == ind :
                tot += curr
        if (n + m ) % 2 == 1:
            return tot
        else:
            return tot / 2
