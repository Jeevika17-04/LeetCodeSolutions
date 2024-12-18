class Solution(object):
    def finalPrices(self, prices):
        s = []
        n = len(prices)

        for i in range(n - 1, -1, -1):
            while s and prices[i] < s[-1]:
                s.pop(-1)

            discount = s[-1] if s else 0
            prices[i] -= discount
            s.append(prices[i] + discount)

        return prices
