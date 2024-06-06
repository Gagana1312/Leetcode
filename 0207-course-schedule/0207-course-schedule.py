class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map each course to the prerequisite lst
        preMap = {i:[] for i in range(numCourses)}
        #crs = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        #visitedSet = all courses along the current path
        vs = set()
        def dfs(crs):
            if crs in vs:
                return False
            if preMap[crs] == []:
                return True
            
            vs.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            vs.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
