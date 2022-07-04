#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # if not intervals:
        #     return []
        # intervals = sorted(intervals, key=lambda x:x[0])
        # res = []
        # start = intervals[0][0]
        # end = intervals[0][1]
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] > end:
        #         res.append([start, end])
        #         start = intervals[i][0]
        #         end = intervals[i][1]
        #     else:
        #         end = max(end, intervals[i][1])
        # res.append([start, end])
        # return res
        
        
        if not intervals:
            return None

        new_intervals = sorted(intervals, key=lambda x: x[0])
        res = [new_intervals[0]]
        for i in range(1, len(new_intervals)):
            if res[-1][1] >= new_intervals[i][0]:
                res[-1][1] = max(res[-1][1], new_intervals[i][1])
            else:
                res.append(new_intervals[i])
        return res



        
                 
# @lc code=end

