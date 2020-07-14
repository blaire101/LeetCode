# -*- coding: utf-8 -*-
"""
    @file: f10_max_long_no_repeat_str.py
    @date: 2020-07-14 7:27 AM
"""


# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
#
#  
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = tmp = i = 0
        for j in range(len(s)):
            i = j - 1
            while i >= 0 and s[i] != s[j]: i -= 1  # 线性查找 i
            tmp = tmp + 1 if tmp < j - i else j - i  # dp[j - 1] -> dp[j]
            res = max(res, tmp)  # max(dp[j - 1], dp[j])
        return res

# 方法二： 动态规划 + 线性遍历
# 左边界 ii 获取方式： 遍历到 s[j]s[j] 时，初始化索引 i = j - 1i=j−1 ，向左遍历搜索第一个满足 s[i] = s[j]s[i]=s[j] 的字符即可 。
# 复杂度分析：
# 时间复杂度 O(N^2)O(N
# 2
#  ) ： 其中 NN 为字符串长度，动态规划需遍历计算 dpdp 列表，占用 O(N)O(N) ；每轮计算 dp[j]dp[j] 时搜索 ii 需要遍历 jj 个字符，占用 O(N)O(N) 。
# 空间复杂度 O(1)O(1) ： 几个变量使用常数大小的额外空间。
