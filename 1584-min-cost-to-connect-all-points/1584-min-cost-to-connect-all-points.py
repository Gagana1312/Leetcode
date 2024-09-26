class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N= len(points)

        adj = { i:[] for i in range(N)} # i:list of[cost, node]
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2)+ abs(y2-y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        #prims
        res = 0
        visit = set()
        minH = [[0,0]] # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        
        return res
        