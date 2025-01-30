class Solution(object):
    def longestCommonPrefix(self, strs):
        s = strs[0]
        n = len(strs)
        for i in range(1,n):
            sn = len(s)
            m = len(strs[i])
            j = 0
            if m < 1:
                return ""
            for j in range(m):
                if  j < sn :
                    if strs[i][j] == s[j]:
                        continue
                    s=s[:j]
                break
            s = s[:j+1]
        return s
