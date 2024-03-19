"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtoNew ={}

        def dfs(node):
            if node in oldtoNew:
                return oldtoNew[node]
            
            clone = Node(node.val)
            oldtoNew[node] = clone
            for ni in node.neighbors:
                clone.neighbors.append(dfs(ni))
            return clone
        
        return dfs(node) if node else None


        