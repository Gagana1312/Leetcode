"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        start = node
        oton ={}
        stk =[start]
        visited=set()
        visited.add(start)

        # creating the new node
        while stk:
            node = stk.pop()
            oton[node] = Node(val = node.val)

            for ni in node.neighbors:
                if ni not in visited:
                    visited.add(ni)
                    stk.append(ni)
        
        # taking the old node refernce, taking the neighbors and helping newnode to attach to its newneighbors.
        for oldnode, newnode in oton.items():
            for ni in oldnode.neighbors:
                newni = oton[ni]
                newnode.neighbors.append(newni)
        
        return oton[start]



        