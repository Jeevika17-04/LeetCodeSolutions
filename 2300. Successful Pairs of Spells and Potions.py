class Solution(object):
    def binarySearch(self, arr, key, n, success):
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
             
            if arr[mid] * key < success:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def successfulPairs(self, spells, potions, success):
        potions.sort()
        result = []
        n = len(potions)
        
        for spell in spells:
            if spell * potions[-1] < success:
                result.append(0)
            else:
                successPoint = self.binarySearch(potions, spell, n, success)
                result.append(n - successPoint)
        
        return result

            
