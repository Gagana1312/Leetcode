# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        q = deque()
        res = []
        ans = []
        value = 0
        q.append(root)
        res.append(root.val)
        while q:
            level = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                # res.append(node.val)
                if node.left: 
                    q.append(node.left)
                    res.append(node.left.val)
                if node.right: 
                    q.append(node.right)
                    res.append(node.right.val)
            ans.append(level)
            res.sort()
            if len(res)>=k:
                value = res[k-1]
        return value
            

        