# -*- coding: utf-8 -*-
"""
    @file: easy.findRepeatNumber.py
    @date: 2020-10-02 10:47 AM
    @desc: 剑指 Offer 03	数组中重复的数字
    @url : https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
"""
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:

        dic = set()

        for i in nums:
            if i in dic:
                return i
            dic.add(i)

        return -1