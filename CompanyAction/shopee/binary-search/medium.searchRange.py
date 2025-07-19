# -*- coding: utf-8 -*-
"""
    @file: medium.searchRange.py
    @date: 2020-09-29 10:44 AM
    @desc: 34. 在排序数组中查找元素的第一个和最后一个位置
    @url : https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        def binSearch(nums, t, flag):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > t:
                    r = mid - 1
                elif nums[mid] < t:
                    l = mid + 1
                else:
                    if flag == "L":
                        r = mid - 1
                    else:
                        l = mid + 1

            if flag == 'L' and r + 1 < len(nums) and nums[r + 1] == t:
                return r + 1
            if flag == 'R' and l - 1 >= 0 and nums[l - 1] == t:
                return l - 1
            return -1

        return [binSearch(nums=nums, t=target, flag='L'), binSearch(nums=nums, t=target, flag='R')]
