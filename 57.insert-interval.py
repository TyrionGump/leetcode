#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        '''
        if not intervals:
            return [newInterval]
        res = []
        intervals.append(newInterval)
        intervals = sorted(intervals, key= lambda x:x[0])
        for i in intervals:
            if not res or i[0] > res[-1][1]:
                res.append(i)
            else:
                res[-1][1] = max(i[1], res[-1][1])
        return res
        '''
        
        # 基于下面方法自己写的版本
        res = []
        start = newInterval[0]
        end = newInterval[1]
        j = 0
        for i in intervals:
            if start > i[1]:
                res.append(i)
            else:
                if end < i[0]:
                    break
                start = min(start, i[0])
                end = max(end, i[1])
            j += 1
        res.append([start, end])
        res += intervals[j:]
        return res
            



        

        '''
        # 因为本身 intervals 已经排好序了而且本身是non-overlapping, 这个方法更好
        start = newInterval[0]
        end = newInterval[1]
        result = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i][1]:
                if end < intervals[i][0]:
                    break
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            else:
                result.append(intervals[i])
            i += 1
        result.append([start, end])
        result += intervals[i:]
        return result
        '''

        

        
        
# @lc code=end

