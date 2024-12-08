class Solution(object):
    def maxTwoEvents(self, events):
        ans = 0
        maxValue = 0
        evts = [] 

        for s, e, v in events:
            evts.append((s, 1, v))
            evts.append((e + 1, 0, v))

        evts.sort()

        for _, isStart, value in evts:
            if isStart:
                ans = max(ans, value + maxValue)
            else:
                maxValue = max(maxValue, value)

        return ans
            