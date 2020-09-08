# -*- coding: utf-8 -*-
"""
    @file: im.minArray.py
    @date: 2020-09-08 10:23 AM
    @desc: 剑指 Offer 11. 旋转数组的最小数字
    @url : https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
"""

# 输入：[3,4,5,1,2]
# 输出：1

from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = (low + high) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]

