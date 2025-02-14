class Solution(object):
    def hasPathSum(self, root, targetSum):
        def findSum(root, tot, target):
            if root:
                tot += root.val
                if tot == target and not root.left and not root.right:
                    return True 
                
                left = findSum(root.left, tot, target)
                if left:
                    return True

                right = findSum(root.right, tot, target)
                if right:
                    return True

            return False
        return findSum(root, 0, targetSum)
