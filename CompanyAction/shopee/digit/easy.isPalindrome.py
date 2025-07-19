# -*- coding: utf-8 -*-
"""
    @file: easy.isPalindrome.py
    @date: 2020-09-29 08:38 AM
    @desc: 9. 回文数
    @url : https://leetcode-cn.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # 1221, 121
        div = 1
        while x // div >= 10:
            div *= 10

        # good, 1000021
        while x > 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div = div // 100

        return True
