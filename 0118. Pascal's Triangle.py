class Solution(object):
    def generate(self, numRows):
        triangle = []

        for i in range(1, numRows + 1):
            curr = []

            for j in range(i):
                if j == i - 1 or j == 0:
                    curr.append(1)
                else:
                   curr.append(triangle[i - 2][j - 1] + triangle[i - 2][j])
    
            triangle.append(curr)
            
        return triangle
