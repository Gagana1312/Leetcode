class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent={i:i for i in range(n)}
        for edge in edges:
            cur_parent = edge[0]
            while cur_parent!=parent[cur_parent]:
                cur_parent=parent[cur_parent]
            parent[edge[1]] = cur_parent
        
        root_parent=0
        while root_parent!=parent[root_parent]:
                root_parent=parent[root_parent] 
        
        for i in range(n):
            find_parent = i
            while find_parent!=parent[find_parent]:
                find_parent=parent[find_parent]
            if find_parent!=root_parent:
                return -1
        
        return root_parent

        