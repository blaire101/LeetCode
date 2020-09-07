# -*- coding: utf-8 -*-
"""
    @file: e.findContinuousSequence.py
    @date: 2020-09-07 8:19 AM
    @desc: 剑指 Offer 57 - II. 和为s的连续正数序列
    @answ: 滑动窗口
"""

from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i = 1 # 滑动窗口的左边界
        j = 1 # 滑动窗口的右边界
        sum = 0 # 滑动窗口中数字的和
        res = []

        while i <= target // 2:
            if sum < target:
                # 右边界向右移动
                sum += j
                j += 1
            elif sum > target:
                # 左边界向右移动
                sum -= i
                i += 1
            else:
                # 记录结果
                arr = list(range(i, j))
                res.append(arr)
                # 左边界向右移动
                sum -= i
                i += 1

        return res

