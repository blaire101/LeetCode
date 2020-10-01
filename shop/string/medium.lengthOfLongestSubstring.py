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

# abcabcbb
# abc

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)

        r = -1  # rk init -1
        ans = 0

        for l in range(n):
            if l != 0:
                occ.remove(s[l - 1])

            while r + 1 < n and s[r + 1] not in occ:
                occ.add(s[r + 1])
                r += 1

            ans = max(ans, r - l + 1)

        return ans
