# -*- coding: utf-8 -*-
"""
    @file: e.spiralOrder.py
    @date: 2020-09-07 4:19 PM
    @desc: 剑指 Offer 29. 顺时针打印矩阵
    @url : https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
"""

# 输入：matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# 输出：[
#     1,2,3,4,
#     8,12,11,10,
#     9,5,6,7
# ]
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1

        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])

            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])

            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])

            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return order

        # 00 01 02 03
        # 13 23
        # 22 21 20
