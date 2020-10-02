# -*- coding: utf-8 -*-
"""
    @file: easy.numWays.py
    @date: 2020-10-02 10:54 AM
    @desc: 剑指 Offer 10- II. 青蛙跳台阶问题
    @url : https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
"""


class Solution:
    def numWays(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1

        a = 1
        b = 1

        for i in range(1, n):
            a, b = b, a + b

        return b % 1000000007