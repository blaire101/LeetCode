# -*- coding: utf-8 -*-
"""
    @file: e.class.sumNums.py
    @date: 2020-09-07 4:19 PM
    @desc: 剑指 Offer 29. 顺时针打印矩阵
"""


class Solution:

    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res