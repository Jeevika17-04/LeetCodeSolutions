class Solution(object):
    def numberOfBeams(self, bank):
        total = 0
        prev = 0
        curr = 0

        for row in bank:
            for cell in row:
                if cell == '1':
                    curr += 1

            if curr != 0:
                total += prev * curr
                prev = curr 
                curr = 0
    
        return total
