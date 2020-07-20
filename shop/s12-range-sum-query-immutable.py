# -*- coding: utf-8 -*-
"""
    @file: s12-range-sum-query-immutable.py
    @date: 2020-07-20 11:00 AM
"""

from typing import List


# 303. 区域和检索 - 数组不可变
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
#
# 示例：
#
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 说明:
#
# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。
#
# @[TOC](303. 区域和检索 - 数组不可变（Range Sum Query - Immutable）)
#
# 题解
# 每次调用函数计算一次都需要O(n)复杂度，因此借助缓存来保存区域和。
# 若使用二维dp，dp[i][j]表示i到j的区域和，需要O(n^{2})
# 2
#  )空间复杂度。
# 考虑以上因素，我们使用一维dp，其中dp[i]表示到i-1索引处的累加和。则易得i到j的区域和公式：
# dp[j+1]-dp[i]
#
# 缓存+动态规划
# 特判，若数组为空，返回。
# 初始化dp=[0,\cdots,0]dp=[0,⋯,0]，长度为n+1n+1。
# 遍历数组，保存累加和，遍历区间[2,n+1)：
# dp[i]=nums[i-1]+dp[i-1]
# 索引ii到jj间的区域和公式：dp[j+1]-dp[i]
# 复杂度分析
# 时间复杂度：O(n)，每次查询只需要O(1)
# 空间复杂度：O(n)
# Python

class NumArray:

    def __init__(self, nums: List[int]):
        if (not nums):
            return
        n = len(nums)
        self.dp = [0] * (n + 1)
        self.dp[1] = nums[0]
        for i in range(2, n + 1):
            self.dp[i] = nums[i - 1] + self.dp[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j + 1] - self.dp[i]
