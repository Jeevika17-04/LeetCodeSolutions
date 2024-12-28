class Solution(object):
    def climbStairs(self, n):
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            return num * factorial(num - 1)

        def combination(n, k):
            return factorial(n) // (factorial(k) * factorial(n - k))

        total_ways = 0
        for k in range(n // 2 + 1):
            total_ways += combination(n - k, k)
        return total_ways
    
