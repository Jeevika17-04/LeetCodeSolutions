class Solution(object):
    def minimizedMaximum(self, n, quantities):
        l = 1
        r = max(quantities)

        def numStores(m):
            return sum((q - 1) // m + 1 for q in quantities)

        while l < r:
            m = (l + r) // 2
            if numStores(m) <= n:
                r = m
            else:
                l = m + 1

        return l
