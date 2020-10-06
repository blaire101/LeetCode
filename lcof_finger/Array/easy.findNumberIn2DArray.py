# -*- coding: utf-8 -*-
"""
    @file: easy.findNumberIn2DArray.py
    @date: 2020-10-06 11:23 AM
    @desc: 剑指 Offer 04. 二维数组中的查找
    @url : https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
"""

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])

        i = 0
        j = col - 1

        while 0 <= i and i < row and 0 <= j and j < col:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return True

        return False
