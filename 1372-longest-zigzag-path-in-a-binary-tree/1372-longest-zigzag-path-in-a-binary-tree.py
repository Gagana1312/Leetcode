# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.summ = 0  
        def dfs(node, dir, length):
            if not node:
                return
            self.summ = max(self.summ, length)
            if dir == 0:  
                dfs(node.left, 0, 1)  
                dfs(node.right, 1, length + 1)  
            else:  # Coming from the right
                dfs(node.left, 0, length + 1)  
                dfs(node.right, 1, 1)  
        dfs(root.left, 0, 1)
        dfs(root.right, 1, 1)

        return self.summ

        
        

        
        