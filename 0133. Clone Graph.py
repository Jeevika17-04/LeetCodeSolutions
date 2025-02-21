from collections import defaultdict
class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        cloneMap = {}

        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]
                
            clone = Node(node.val)
            cloneMap[node] = clone

            for i in node.neighbors:
                clone.neighbors.append(dfs(i))
            
            return clone
        
        return dfs(node)
