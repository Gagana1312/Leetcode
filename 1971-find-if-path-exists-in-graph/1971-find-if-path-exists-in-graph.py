class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # DFS with recursion

        if source == destination:
            return True
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited= set()
        visited.add(source)

        def dfs(i):
            if i == destination:
                return True
            
            for next_node in graph[i]:
                if next_node not in visited:
                    visited.add(next_node)
                    if dfs(next_node):
                        return True
            
            return False

        return dfs(source)



        



        