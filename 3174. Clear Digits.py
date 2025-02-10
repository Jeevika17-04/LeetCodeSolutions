from collections import deque
class Solution(object):
    def clearDigits(self, s):
        res = deque()
        for i in s:
            if i.isdigit():
                res.pop()
            else:
                res.append(i)
        return "".join(res)
