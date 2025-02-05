class Solution(object):
    def areAlmostEqual(self, s1, s2):
        count = 0
        ind = []
        n = len(s2)
        for i in range(n):
            if s1[i] != s2[i]:
                count += 1
                ind.append(i)
            if count > 2:
                return False
        if len(ind) % 2 != 0:
            return False
        elif len(ind) == 0:
            return True
        return True if s1[ind[0]] == s2[ind[1]] and s1[ind[1]] == s2[ind[0]] else False
