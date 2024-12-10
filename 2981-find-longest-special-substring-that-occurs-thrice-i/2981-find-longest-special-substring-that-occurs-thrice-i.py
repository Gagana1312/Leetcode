class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        runningLen = 0
        prevLetter = '@'
        # counts[i][j] := the frequency of ('a' + i) repeating j times
        counts = [[0] * (n + 1) for _ in range(26)]

        for c in s:
          if c == prevLetter:
            runningLen += 1
            counts[string.ascii_lowercase.index(c)][runningLen] += 1
          else:
            runningLen = 1
            counts[string.ascii_lowercase.index(c)][runningLen] += 1
            prevLetter = c

        def getMaxFreq(count):
          times = 0
          for freq in range(n, 0, -1):
            times += count[freq]
            if times >= 3:
              return freq
          return -1

        return max(getMaxFreq(count) for count in counts)
        