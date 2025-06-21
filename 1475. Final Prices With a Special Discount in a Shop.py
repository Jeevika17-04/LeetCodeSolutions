class Solution(object):
    def finalPrices(self, prices):
        s = []
        n = len(prices)
        for i in range(n):
            while s and prices[s[-1]] >= prices[i]:
                index = s.pop(-1)
                prices[index] -= prices[i]
            
            s.append(i)

        return prices
