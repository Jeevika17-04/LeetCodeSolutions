class Solution(object):
    def stringHash(self, s, k):
        n = len(s)
        res = ""

        d = {letter: i for i, letter in enumerate(string.ascii_lowercase)}
        total = 0
        count = 0

        for i in range(n):
            if count == k:
                res += chr(97 + total % 26)
                total = 0                
                count = 0
            
            total += d[s[i]]
            count += 1
        res += chr(97 + total % 26)

        return res
