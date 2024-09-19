# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if (root and not root2) or (root2 and not root1) or (not root1 or not root2):
                return False
            if root1.val!= root2.val:
                return False
            return (dfs(root1.left, root2.right) and dfs(root1.right, root2.left))
        return dfs(root, root)

        