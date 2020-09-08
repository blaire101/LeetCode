# -*- coding: utf-8 -*-
"""
    @file: e.minNumber.py
    @date: 2020-09-08 11:01 AM
    @desc: 剑指 Offer 45. 把数组排成最小的数
    @url : https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
"""

from functools import cmp_to_key
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=cmp_to_key(sort_rule))
        return ''.join(strs)


