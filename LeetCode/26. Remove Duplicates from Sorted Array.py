"""
26. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        lens = len(nums) - 1

        while lens >= 0:
            if nums.count(nums[lens]) > 1:
                nums.remove(nums[lens])
            lens -= 1
        return len(nums)


# for test
s = [1,1,1,1]
sol = Solution().removeDuplicates(s)
print(sol)