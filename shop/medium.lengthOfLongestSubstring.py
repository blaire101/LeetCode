# -*- coding: utf-8 -*-
"""
    @file: medium.lengthOfLongestSubstring.py
    @date: 2020-09-24 08:38 AM
    @desc: 无重复字符的最长子串
    @url : https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""

# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        dp = {}
        len1 = len(s)
        for i in range(len1):
            pass