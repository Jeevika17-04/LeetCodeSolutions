class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):

        def createGraph(prerequisites, numCourses):
            adj = [[] for i in range(numCourses)]
            for i in prerequisites:
                adj[i[1]].append(i[0])

            return adj
        
        def check(i, j, pre, n):
            q = []
            q.append(j)
            visited = [False] * n
            visited[j] = True

            while q:
                ele = q.pop(0)
                for k in pre[ele]:

                    if not visited[k]:
                        q.append(k)
                        visited[k] = True

                    if k == i:
                        return True
            return False

        pre = createGraph(prerequisites, numCourses)
        result = []

        for i in queries:
            result.append(check(i[0], i[1], pre, numCourses))
                 
        return result
