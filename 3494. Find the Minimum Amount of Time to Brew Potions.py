class Solution(object):
    def minTime(self, skill, mana):
        n, m = len(skill), len(mana)
        total = sum(skill)
        res = total * mana[0]
        for j in range(1, m):
            prev = res
            for i in range(n - 2, -1, -1):
                prev -= skill[i + 1] * mana[j - 1]
                res = max(prev, res - skill[i] * mana[j])
            res += total * mana[j]
        return res
