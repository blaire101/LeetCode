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

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (high - low) // 2 + low

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return -1
