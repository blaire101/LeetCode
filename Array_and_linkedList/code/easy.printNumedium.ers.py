# -*- coding: utf-8 -*-
"""
    @file: e.printNumbers.py
    @date: 2020-09-06 10:25 PM
"""

from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:

        res = []

        sum = 10 ** n
        
        for i in range(1, sum):
            res.append(i)

        return res


if __name__ == '__main__':
    sb = Solution()
    
    sb.printNumbers(2)