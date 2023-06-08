"""
1351. Count Negative Numbers in a Sorted Matrix
link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
"""


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        counter = 0
        max_len = len(grid)

        while max_len > 0:
            for i in range(len(grid[0])):
                if grid[max_len - 1][i] < 0:
                    counter += 1
            max_len -= 1
        return counter


if __name__ == '__main__':
    g = [[5, 1, 0], [-5, -5, -5]]
    s = Solution().countNegatives(g)
    print(s)