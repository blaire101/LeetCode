
# -*- coding: utf-8 -*-
"""
    @file: im.movingCount.py
    @date: 2020-09-08 11:56 AM
    @desc: 剑指 Offer 13. 机器人的运动范围
    @url : https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
"""


# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
#  
#
# 示例 1：
#
# 输入：m = 2, n = 3, k = 1
# 输出：3
# 示例 2：
#
# 输入：m = 3, n = 1, k = 0
# 输出：1
#

from queue import Queue


def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


def is_valid_position(x, y, n, m, k, s):
    if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
        return True
    return False


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        q = Queue()
        q.put((0, 0))
        s = set()
        s.add((0,0))
        while not q.empty():
            x, y = q.get()
            for nx, ny in [(x + 1, y), (x, y + 1)]:
                if not is_valid_position(nx, ny, n, m, k, s):
                    continue
                s.add((nx, ny))
                q.put((nx, ny))
        return len(s)