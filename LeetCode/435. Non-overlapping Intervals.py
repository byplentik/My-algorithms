"""
435. Non-overlapping Intervals
link: https://leetcode.com/problems/non-overlapping-intervals/
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        end = intervals[0][1]
        count = len(intervals) - 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count -= 1
        return count

if __name__ == '__main__':
    arg = [[1,100],[11,22],[1,11],[2,12]]
    sol = Solution().eraseOverlapIntervals(arg)
    print(sol)