# -*- coding: utf-8 -*-
"""
    @file: f7_sum_continue_num.py
    @date: 2020-07-13 11:07 AM
"""

from typing import List

#
# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#
#  
#
# 示例 1：
#
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
# 示例 2：
#
# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#
# def findContinuousSequence(self, target: int) -> List[List[int]]:
#     i = 1 # 滑动窗口的左边界
#     j = 1 # 滑动窗口的右边界
#     sum = 0 # 滑动窗口中数字的和
#     res = []
#
#     while i <= target // 2:
#         if sum < target:
#             # 右边界向右移动
#             sum += j
#             j += 1
#         elif sum > target:
#             # 左边界向右移动
#             sum -= i
#             i += 1
#         else:
#             # 记录结果
#             arr = list(range(i, j))
#             res.append(arr)
#             # 左边界向右移动
#             sum -= i
#             i += 1
#
#     return res

'''https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/'''


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target <= 2:  # 最小的target应该是3 -> [1, 2]
            return []
        res = []
        for n in range(2, target + 1):  # n -> 首尾间隔
            temp = target - n * (n - 1) // 2
            if temp <= 0:
                break
            if not temp % n:  # 首项必为正整数
                start = temp // n
                res.append([start + i for i in range(n)])
        return res[::-1]
