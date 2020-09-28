# -*- coding: utf-8 -*-
"""
    @file: easy.isValid.py
    @date: 2020-09-18 08:38 AM
    @desc: 有效的括号
    @url : https://leetcode-cn.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:

            if i in ['(', '[', '{']:
                stack.append(i)
            elif i == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif i == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            elif i == '}' and len(stack)> 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False

        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()
    s = "()"
    print(sol.isValid(s))
