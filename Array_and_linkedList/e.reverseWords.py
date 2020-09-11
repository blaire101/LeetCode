# -*- coding: utf-8 -*-
"""
    @file: e.reverseWords
    @date: 2020-09-11 8:44 PM
    @desc: 剑指 Offer 58 - I. 翻转单词顺序
    @url : https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        strs = s.split() # 分割字符串
        strs.reverse() # 翻转单词列表
        return ' '.join(strs) # 拼接为字符串并返回

