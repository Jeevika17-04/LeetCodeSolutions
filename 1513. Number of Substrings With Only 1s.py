import math
class Solution(object):
    def numSub(self, s):
        MOD =  (10 ** 9) + 7
        result = 0
        count = 0

        for ch in s:
            if ch == '1':
                count += 1
                result += count
            else:
                count = 0

        return result % MOD  
