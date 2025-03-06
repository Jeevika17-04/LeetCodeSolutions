class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        visited = [False] * (n * n)
        res = []

        for i in grid:
            for j in i:
                if visited[j - 1]:
                    res.append(j)
                visited[j - 1] = True
        
        for i in range(n * n):
            if not visited[i]:
                res.append(i + 1)
        
        return res
