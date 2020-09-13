# -*- coding: utf-8 -*-
"""
    @file: medium.maxProfit.py
    @date: 2020-09-13 8:26 AM
    @desc: 剑指 Offer 63. 股票的最大利润
    @answ: https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian-shi-ti-63-gu-piao-de-zui-da-li-run-dong-tai-2/
    @url : https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cost, profit = float("+inf"), 0

        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)

        return profit

