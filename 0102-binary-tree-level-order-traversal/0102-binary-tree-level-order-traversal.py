# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque()
        q.append(root)
        ans=[]
        while q:
            level =[]
            n = len(q)
            for i in range(n):
                node = q.popleft()
                level.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(level)
        return ans


        