# -*- coding: utf-8 -*-
"""
    @file: e.hammingWeight.py
    @date: 2020-09-07 8:17 AM
    @desc: 剑指 Offer 15. 二进制中1的个数
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            n = n & (n - 1)
            res += 1

        return res
