class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # res =[]
        # intervals = sorted(intervals, key=lambda x: x[0])
        # i=0
        # while i < len(intervals):
            
        #     if i<len(intervals)-1  and intervals[i][0]<=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][0] and intervals[i][1]<=intervals[i+1][1]:
        #         res.append([intervals[i][0], intervals[i+1][1]])
        #         i+=1
        #     elif i<len(intervals)-1 and intervals[i][1]<=intervals[i+1][0]:
        #         res.append(intervals[i])
        #         res.append(intervals[i+1])
        #         i+=1
        #     else:
        #         res.append(intervals[i])
        #     i+=1
        # return res



        merge = []
        intervals.sort(key = lambda interval: interval[0])

        for interval in intervals:
            if not merge or merge[-1][1]<interval[0]:
                merge.append(interval)
            else:
                merge[-1] = [merge[-1][0], max(merge[-1][1], interval[1])]
        return merge


        # for i in intervals:
        #     if not res or res[-1][1]<i[0]:
        #         res.append(i)
        #     else:
        #         res[-1] = [res[-1][0], max(res[-1][1],i[1])]
        # return res
        
        
        
        # res = []
        # if not intervals:
        #     return res
        # if len(intervals) == 1:
        #     return intervals
        # intervals = sorted(intervals, key=lambda x: x[0])

        # i = 0
        # while i < len(intervals):
        #     current_start, current_end = intervals[i]
        #     while i < len(intervals) - 1 and intervals[i + 1][0] <= current_end:
        #         current_end = max(current_end, intervals[i + 1][1])  
        #         i += 1
        #     res.append([current_start, current_end])
        #     i += 1
        # return res
            










                


        