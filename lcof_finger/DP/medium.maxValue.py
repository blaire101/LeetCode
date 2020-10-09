# -*- coding: utf-8 -*-
"""
    @file: medium.maxValue.py
    @date: 2020-10-09 3:43 PM
    @desc: 剑指 Offer 47. 礼物的最大价值
    @url : https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
"""
from typing import List


class Solution:

    def __init__(self):
        pass

    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        f = [len(grid[0]) * [0]] * len(grid)

        f[0][0] = grid[0][0]

        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    f[i][j] = f[i][j - 1] + grid[i][j]
                elif j == 0:
                    f[i][j] = f[i - 1][j] + grid[i][j]
                else:
                    f[i][j] = max(f[i][j - 1], f[i - 1][j]) + grid[i][j]

        return f[row-1][col-1]
