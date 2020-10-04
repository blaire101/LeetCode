# -*- coding: utf-8 -*-
"""
    @file: easy.reverseLeftWords.py
    @date: 2020-09-06 10:15 PM
"""


# 输入: s = "abcdefg", k = 2
# 输出: "cdefgab"

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
