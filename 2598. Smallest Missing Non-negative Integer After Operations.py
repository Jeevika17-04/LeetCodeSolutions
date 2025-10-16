class Solution(object):
    def findSmallestInteger(self, nums, value):
        arr = [0] * value
        
        for num in nums:
            arr[num % value] += 1
        
        smallest = 0
        for i in range(value):
            if arr[i] == 0:
                return i
            
            if arr[i] < arr[smallest]:
                smallest = i
        
        return (arr[smallest] * value) + smallest
