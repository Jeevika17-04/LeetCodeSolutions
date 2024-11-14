class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxi = 0
        a = 0
        n = len(s)
        for i in range(n):
            d=set()
            a = 0
            while i < n:
                if s[i] not in d:
                    d.add(s[i])
                    a += 1
                    i += 1
                else:
                    break
            if a > maxi:
                maxi = a
        if a > maxi :
            return a
        return maxi
