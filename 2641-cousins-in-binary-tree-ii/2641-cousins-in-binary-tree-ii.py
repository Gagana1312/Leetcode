# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        # Use a queue for level order traversal
        queue = deque([(root, None)])  # (node, parent)
        
        # Level-order traversal
        while queue:
            level_size = len(queue)
            total_sum = 0
            level_parents = defaultdict(list)  # Stores nodes by their parent
            
            # Calculate the sum of the current level and organize nodes by parent
            for _ in range(level_size):
                node, parent = queue.popleft()
                total_sum += node.val
                level_parents[parent].append(node)
                
                # Add children to the queue
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            
            # Replace each node's value with the sum of all its cousins' values
            for nodes in level_parents.values():
                sibling_sum = sum(node.val for node in nodes)
                for node in nodes:
                    node.val = total_sum - sibling_sum
        
        return root
        