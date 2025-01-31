class Solution(object):
    def strStr(self, haystack, needle):
        occurance = []
        n, m = len(haystack), len(needle)
        i = 0
        ind = 0

        while i <= n - m:
            if len(occurance) > ind:
               i = occurance[ind]
               ind += 1
               
            if needle[0] == haystack[i]:
                j = 1
                flag = True
                while j < m:
                    if needle[0] == haystack[j + i]:
                        occurance.append(i + j)
                    if needle[j] != haystack[i + j ]:
                        flag = False
                        break
                    j += 1
                if flag:
                    return i
            i += 1
        return -1
