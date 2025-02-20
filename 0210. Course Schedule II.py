class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        g = [[] for i in range(numCourses)]
        q = []
        res = []

        indegree = [0] * numCourses

        for i, j in prerequisites:
            indegree[i] += 1
            g[j].append(i)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        while q:
            v = q.pop(0)
            res.append(v)
            for i in g[v]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        
        return res if len(res) == numCourses else []
