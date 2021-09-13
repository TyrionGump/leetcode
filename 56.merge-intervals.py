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
        '''
        if not intervals or len(intervals) == 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        mergedIntervals = []
        
        for interval in intervals:
            if not mergedIntervals or interval[0] > mergedIntervals[-1][1]:
                mergedIntervals.append(interval)
            else:
                mergedIntervals[-1][1] = max(interval[1], mergedIntervals[-1][1])
        
        return mergedIntervals
        '''

        
                 
# @lc code=end

