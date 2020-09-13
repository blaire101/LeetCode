# -*- coding: utf-8 -*-
"""
    @file: e.isStraight.py
    @date: 2020-09-10 10:19 AM
    @desc: 剑指 Offer 61. 扑克牌中的顺子
    @url : https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
"""
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue # 跳过大小王
            ma = max(ma, num) # 最大牌
            mi = min(mi, num) # 最小牌
            if num in repeat: return False # 若有重复，提前返回 false
            repeat.add(num) # 添加牌至 Set
        return ma - mi < 5 # 最大牌 - 最小牌 < 5 则可构成顺子
