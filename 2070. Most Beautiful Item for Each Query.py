from bisect import bisect_right
class Solution(object):
    def maximumBeauty(self, items, queries):
        items.sort(key=lambda x: (x[0], -x[1]))

        prices = []
        max_beauties = []
        
        max_beauty = 0
        for price, beauty in items:
            if not prices or price != prices[-1]:
                prices.append(price)
                max_beauty = max(max_beauty, beauty)
                max_beauties.append(max_beauty)
            else:
                max_beauty = max(max_beauty, beauty)
                max_beauties[-1] = max_beauty

        res = []
        for q in queries:
            idx = bisect_right(prices, q) - 1
            res.append(max_beauties[idx] if idx >= 0 else 0)

        return res
