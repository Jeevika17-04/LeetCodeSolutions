class Solution(object):
    def queryResults(self, limit, queries):
        n = len(queries)
        colours = {}
        balls = {}

        res = []
        for i in range(n):
            pos, col = queries[i]
            
            if pos in balls:
                prev_col = balls[pos]
                colours[prev_col] -= 1
                if colours[prev_col] == 0:
                    del colours[prev_col]

            balls[pos] = col
            colours[col] = colours.get(col, 0) + 1

            res.append(len(colours))

        return res
