# -*- coding: utf-8 -*-
"""
    @file: e.firstUniqChar.py
    @date: 2020-09-07 2:35 PM
    @desc: 剑指 Offer 50. 第一个只出现一次的字符
    @url : https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
"""

# s = "abaccdeff"
# 返回 "b"
#
# s = ""
# 返回 " "

# Python 3.6 后，默认字典就是有序的，因此无需使用 OrderedDict()
#
# 详情可见：为什么Python 3.6以后字典有序并且效率更高？
# https://www.cnblogs.com/xieqiankun/p/python_dict.html


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic

        for k, v in dic.items():
            if v: return k

        return ' '

