# -*- coding: utf-8 -*-
"""
    @file: medium.lengthOfLongestSubstring.py
    @date: 2020-09-12 12:50 PM
    @desc: 剑指 Offer 48. 最长不含重复字符的子字符串
    @answ: https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/solution/tu-jie-hua-dong-chuang-kou-shuang-zhi-zhen-shi-xia/
    @url : https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
"""


# 思路一 ：滑动窗口（双指针）
# 题目中要求答案必须是 子串 的长度，意味着子串内的字符在原字符串中一定是连续的。因此我们可以将答案看作原字符串的一个滑动窗口，并维护窗口内不能有重复字符，同时更新窗口的最大值。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        tail = 0
        if len(s) < 2: return len(s)  # 边界条件
        res = 1

        while tail < len(s) - 1:
            tail += 1
            if s[tail] not in s[head: tail]:
                res = max(tail - head + 1, res)
            else:
                while s[tail] in s[head: tail]:
                    head += 1
        return res


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         hashmap = {}
#         head, res = 0, 0
#         for tail in range(n):
#             if s[tail] in hashmap:
#                 head = max(hashmap[s[tail]], head)
#             hashmap[s[tail]] = tail + 1
#             res = max(res, tail - head + 1)
#         return res
