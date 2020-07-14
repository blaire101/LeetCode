# -*- coding: utf-8 -*-
"""
    @file: f12_12n.py
    @date: 2020-07-14 7:57 AM
"""


# 面试题64. 求 1 + 2 + … + n（逻辑符短路，清晰图解）

class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res
