class Solution(object):
    def prisonAfterNDays(self, cells, n):
        curr = [0] * 8
        n = n % 14 or 14

        for i in range(n):
            curr[0] = 0
            curr[7] = 0
            for j in range(1, 7):
                curr[j] = 1 if cells[j - 1] == cells[j + 1] else 0
            
            curr, cells = cells, curr
        
        return cells
