# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def dfs(node, current_sum):
            if not node:
                return 0
            
            count = 1 if current_sum + node.val == targetSum else 0
            count += dfs(node.left, current_sum + node.val)
            count += dfs(node.right, current_sum + node.val)
            
            return count

        if not root:
            return 0
        
        paths_from_root = dfs(root, 0)
        paths_in_left_subtree = self.pathSum(root.left, targetSum)
        paths_in_right_subtree = self.pathSum(root.right, targetSum)
        
        return paths_from_root + paths_in_left_subtree + paths_in_right_subtree
