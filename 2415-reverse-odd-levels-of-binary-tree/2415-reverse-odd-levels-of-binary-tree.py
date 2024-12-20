# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        queue = deque([root])
        level = 0
        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse values of nodes at odd levels
            if level % 2 == 1:
                for i in range(len(current_level) // 2):
                    current_level[i].val, current_level[-i-1].val = current_level[-i-1].val, current_level[i].val

            level += 1

        return root
        
        
        
            
        