# -*- coding: utf-8 -*-
"""
    @file: se.fib.py
    @date: 2020-09-10 10:19 AM
    @desc: 剑指 Offer 10- I. 斐波那契数列
    @url : https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
"""

N = 1000000007

dp = {}

class Solution:
    def __init__(self):
        dp[0] = 0
        dp[1] = 1
        for i in range(2, 100):
            dp[i] = (dp[i-1] + dp[i-2]) % N

    def fib(self, n: int) -> int:
        return dp[n]




