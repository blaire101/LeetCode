# -*- coding: utf-8 -*-
"""
    @file: medium.coinChange.py
    @date: 2020-09-21 9:16 AM
    @desc: 零钱兑换
    @url : https://leetcode-cn.com/problems/coin-change/
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
