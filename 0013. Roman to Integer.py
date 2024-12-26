class Solution(object):
    def romanToInt(self, s):
        n = len(s)
        i = n - 1
        values = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        num = 0 
        prev = 0
        while i >= 0:
            curr = values[s[i]]
            if curr < prev:
                num -= curr
            else:
                num += curr
                
            i -= 1
            prev = curr
        
        return num
