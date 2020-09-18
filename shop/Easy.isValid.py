# -*- coding: utf-8 -*-
"""
    @file: Easy.isValid.py
    @date: 2020-09-18 08:38 AM
    @desc: 有效的括号
    @url : https://leetcode-cn.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack= []

        if not s:
            return True

        for c in s:
            stack.append(c)

if __name__ == '__main__':
    sol = Solution()
    sol.isValid("([])")
