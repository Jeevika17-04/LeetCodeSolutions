from collections import deque

class Solution(object):
    def containsCycle(self, grid):
        def isCycle(x, y):
            q = deque([(x, y, -1, -1)])  
            visited[x][y] = True

            while q:
                i, j, prev_i, prev_j = q.popleft()
                for k in range(4):
                    ni, nj = i + r[k], j + c[k]
                    if (ni, nj) == (prev_i, prev_j):
                        continue
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == grid[i][j]:
                        if visited[ni][nj]:
                            return True  
                        q.append((ni, nj, i, j))
                        visited[ni][nj] = True
            return False

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        r, c = [-1, 0, 1, 0], [0, 1, 0, -1]

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and isCycle(i, j):
                    return True
        
        return False
