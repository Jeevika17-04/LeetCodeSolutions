class Solution(object):
    def findMaxFish(self, grid):

        def hasWater(i, j, m, n, grid):
            if 0 <= i < m and 0 <= j < n and grid[i][j] > 0:
                return True
            return False
        
        def findFish(grid, m, n, i, j, r, c):
            q = [(i, j)]
            fish = grid[i][j]
            grid[i][j] = 0

            while q:
                i, j = q.pop(0)

                for k in range(4):
                    if hasWater(i + r[k], j + c[k], m, n, grid):
                        q.append((i + r[k], j + c[k]))
                        fish += grid[i + r[k]][j + c[k]]
                        grid[i + r[k]][j + c[k]] = 0
            
            return fish

        m = len(grid)
        n = len(grid[0])
        q = []
        max_fish = 0
        c = [-1, 0, 1, 0]
        r = [0, -1, 0, 1]

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    count = findFish(grid, m, n, i, j, r, c)
                    max_fish = max(count, max_fish)

        return max_fish
