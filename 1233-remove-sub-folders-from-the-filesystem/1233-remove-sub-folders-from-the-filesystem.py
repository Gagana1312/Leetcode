class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        res = [folder[0]]  

        for i in range(1, len(folder)):
            if not folder[i].startswith(res[-1] + "/"):
                res.append(folder[i])
        return res
                    
        