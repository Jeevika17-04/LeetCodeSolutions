class Solution(object):
    def connect(self, root):
        def findLevel(root, level):
            if root:
                if len(q) <= level:
                    q.append(None) 

                if q[level] != None:
                    q[level].next = root
                q[level] = root

                findLevel(root.left, level + 1)
                findLevel(root.right, level + 1)
        
        q = []
        findLevel(root, 0)

        return root
