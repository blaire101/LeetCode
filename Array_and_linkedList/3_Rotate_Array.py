# -*- coding: utf-8 -*-
"""
    @file: 3_Rotate_Array.py
    @date: 2019-12-22 16:41
"""

from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, s, e):
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1


if __name__ == '__main__':
    pass
