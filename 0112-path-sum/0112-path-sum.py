# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        def dfs(root, cur_sum):
            if not root:
                return False
            cur_sum+=root.val
            if not root.left and not root.right:
                return cur_sum == targetSum
            return (dfs(root.left, cur_sum) or dfs(root.right, cur_sum))
        return dfs(root,0)
        