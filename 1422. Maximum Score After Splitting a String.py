class Solution(object):
    def maxScore(self, s):
        n = len(s)
        left = right = result = 0
        for i in s:
            if i == '1':
                right += 1
                
        for i in range(n - 1):
            if s[i] == '1':
                right -= 1
            elif s[i] == '0':
                left += 1

            if left + right > result:
                result = left + right

        return result
