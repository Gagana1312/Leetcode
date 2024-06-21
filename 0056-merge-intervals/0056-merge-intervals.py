class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # for i in range(len(intervals)-2):
        #     if intervals[i][1]>intervals[i+1][0]:
        #         intervals[i]=[intervals[i][0],intervals[i+1][1]]
        #         intervals.remove(intervals[i+1])
        # return intervals

        #O(nlogn)

        intervals.sort(key=lambda i : i[0])
        res =[intervals[0]]

        for start,end in intervals[1:]:
            prev_end = res[-1][1]
            if start <= prev_end:
                res[-1][1] = max(prev_end,end)
            else:
                res.append([start,end])

        return res







        


        