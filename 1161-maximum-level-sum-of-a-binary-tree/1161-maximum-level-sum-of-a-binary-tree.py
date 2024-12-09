# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if not root:
            return 0 
        
        q = deque([root]) 
        max_sum = float('-inf')  
        max_level = 1 
        level = 1 

        while q:
            level_sum = 0
            for _ in range(len(q)): 
                node = q.popleft()  
                level_sum += node.val  
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1  

        return max_level
                

        