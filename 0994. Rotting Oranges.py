from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        
        def isValid(m, n, i, j, visited, maze):
            return 0 <= i < m and 0 <= j < n and not visited[i][j] and maze[i][j] == "."
        
        def isExit(i, j, enrtrance):
            return (i == 0 or i == m - 1 or j == 0 or j == n - 1) and (entrance[0] != i or entrance[1] != j)

        i = 0
        m = len(maze)
        n = len(maze[0])
        visited = [[False] * n for i in range(m)]

        distance = float("inf")
        q = deque()
        q.append([entrance[0], entrance[1], 0])
        visited[entrance[0]][entrance[1]] = True
        r = [-1, 0, 1, 0]
        c = [0, 1, 0, -1]

        while q:
            i, j, d = q.popleft()
            for k in range(4):
                if isValid(m, n, i + r[k] , j + c[k], visited, maze):
                    visited[i + r[k]][j + c[k]] = True
                    if isExit(i + r[k], j + c[k], entrance):
                        distance = min(distance, d + 1)
                        continue
                    q.append([i + r[k], j + c[k], d + 1])
        
        return distance if distance != float('inf') else -1
