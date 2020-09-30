# -*- coding: utf-8 -*-
"""
    @file: easy.binary-search.py
    @date: 2020-09-27 3:43 PM
    @desc: 704. 二分查找
    @url : https://leetcode-cn.com/problems/binary-search/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid

        return -1
