# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # q = deque()
        # res = []
        # ans = []
        # value = 0
        # q.append(root)
        # res.append(root.val)
        # while q:
        #     level = []
        #     n = len(q)
        #     for i in range(n):
        #         node = q.popleft()
        #         level.append(node.val)
        #         # res.append(node.val)
        #         if node.left: 
        #             q.append(node.left)
        #             res.append(node.left.val)
        #         if node.right: 
        #             q.append(node.right)
        #             res.append(node.right.val)
        #     ans.append(level)
        #     res.sort()
        #     if len(res)>=1:
        #         value = abs(res[0]-res[1])
        # return value

        mindist = [float('inf')]
        prev = [None]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if prev[0] is not None:
                mindist[0]=min(mindist[0],node.val-prev[0])
            
            prev[0] = node.val
            dfs(node.right)
        dfs(root)
        return mindist[0]
        