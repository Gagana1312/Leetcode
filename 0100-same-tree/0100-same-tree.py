# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def dfs(p,q):
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val != q.val:
                return False
            return dfs(p.left,q.left) and dfs(p.right,q.right)

        return dfs(p,q)


            

        