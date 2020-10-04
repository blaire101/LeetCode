# -*- coding: utf-8 -*-
"""
    @file: easy.lastRemaining.py
    @date: 2020-09-07 11:54 AM
    @desc: 剑指 Offer 62\. 圆圈中最后剩下的数字
    @url : https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
"""

# 输入: n = 5, m = 3
# 输出: 3
# 0, 1, 2, 3, 4
# 题目中的要求可以表述为：给定一个长度为 n 的序列，每次向后数 m 个元素并删除，那么最终留下的是第几个元素？
#
# 这个问题很难快速给出答案。但是同时也要看到，这个问题似乎有拆分为较小子问题的潜质：如果我们知道对于一个长度 n - 1 的序列，留下的是第几个元素，那么我们就可以由此计算出长度为 n 的序列的答案。
#
# 算法
#
# 我们将上述问题建模为函数 f(n, m)，该函数的返回值为最终留下的元素的序号。
#
# 首先，长度为 n 的序列会先删除第 m % n 个元素，然后剩下一个长度为 n - 1 的序列。那么，我们可以递归地求解 f(n - 1, m)，就可以知道对于剩下的 n - 1 个元素，最终会留下第几个元素，我们设答案为 x = f(n - 1, m)。
#
# 由于我们删除了第 m % n 个元素，将序列的长度变为 n - 1。当我们知道了 f(n - 1, m) 对应的答案 x 之后，我们也就可以知道，长度为 n 的序列最后一个删除的元素，应当是从 m % n 开始数的第 x 个元素。因此有 f(n, m) = (m % n + x) % n = (m + x) % n。
# Python 默认的递归深度不够，需要手动设置

import sys

# Python解释器默认对递归深度设定为998，但可以用sys.setrecursionlimit(99999999)来打破这个限制。
sys.setrecursionlimit(100000)


def f(n, m):
    if n == 0:
        return 0
    x = f(n - 1, m)
    return (m % n + x) % n

    # return (m + x) % n


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return f(n, m)

# class Solution:
#     def lastRemaining(self, n: int, m: int) -> int:
#         f = 0
#         for i in range(2, n + 1):
#             f = (m + f) % i
#         return f
