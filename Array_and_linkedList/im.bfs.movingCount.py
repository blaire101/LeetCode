# -*- coding: utf-8 -*-
"""
    @file: im.bfs.movingCount.py
    @date: 2020-09-08 11:56 AM
    @desc: 剑指 Offer 13. 机器人的运动范围
    @url : https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
"""

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

