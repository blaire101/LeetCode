# -*- coding: utf-8 -*-
"""
    @file: s19_longestPalindrome.py
    @date: 2020-07-28 10:15 AM
    @desc: https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
"""

# 5. 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
#
# 📖文字题解
# 方法一：动态规划
# 思路与算法
#
# 对于一个子串而言，如果它是回文串，并且长度大于 2，那么将它首尾的两个字母去除之后，它仍然是个回文串。例如对于字符串 \textrm
# {``ababa
# ''}“ababa”，如果我们已经知道 \textrm
# {``bab
# ''}“bab” 是回文串，那么 \textrm
# {``ababa
# ''}“ababa” 一定是回文串，这是因为它的首尾两个字母都是 \textrm
# {``a
# ''}“a”。
#
# 根据这样的思路，我们就可以用动态规划的方法解决本题。我们用
# P(i, j)
# P(i, j)
# 表示字符串
# ss
# 的第
# ii
# 到
# jj
# 个字母组成的串（下文表示成
# s[i:j]
# s[i:j]）是否为回文串：
#
# P(i, j) = \begin
# {cases} \text
# {true, } &\quad\text
# {如果子串
# ~} S_i \dots
# S_j \text
# {~是回文串}\\ \text
# {false, } &\quad\text
# {其它情况} \end
# {cases}
# P(i, j) = {
#     true,
#     false,
# ​
#
# 如果子串 S
# i
# ​
# …S
# j
# ​
#  是回文串
# 其它情况
# ​
#
#
# 这里的「其它情况」包含两种可能性：
#
# s[i, j]
# s[i, j]
# 本身不是一个回文串；
#
# i > ji > j，此时
# s[i, j]
# s[i, j]
# 本身不合法。
#
# 那么我们就可以写出动态规划的状态转移方程：
#
# P(i, j) = P(i + 1, j - 1) \wedge(S_i == S_j)
# P(i, j) = P(i + 1, j−1)∧(S
#                          i
#                          ​
#                          == S
#                          j
#                          ​
#                          )
#
# 也就是说，只有
# s[i + 1:j - 1]
# s[i + 1:j−1] 是回文串，并且
# ss
# 的第
# ii
# 和
# jj
# 个字母相同时，s[i:j]
# s[i:j]
# 才会是回文串。
#
# 上文的所有讨论是建立在子串长度大于
# 22
# 的前提之上的，我们还需要考虑动态规划中的边界条件，即子串的长度为
# 11
# 或
# 22。对于长度为
# 11
# 的子串，它显然是个回文串；对于长度为
# 22
# 的子串，只要它的两个字母相同，它就是一个回文串。因此我们就可以写出动态规划的边界条件：
#
# \begin
# {cases}
# P(i, i) = \text
# {true} \\ P(i, i + 1) = (S_i == S_{i+1}) \end
# {cases}
# {
#     P(i, i) = true
# P(i, i + 1) = (S
#                i
#                ​
#                == S
#                i+1
#                ​
#                )
# ​
#
#
# 根据这个思路，我们就可以完成动态规划了，最终的答案即为所有
# P(i, j) = \text
# {true}
# P(i, j) = true
# 中
# j - i + 1j−i + 1（即子串长度）的最大值。注意：在状态转移方程中，我们是从长度较短的字符串向长度较长的字符串进行转移的，因此一定要注意动态规划的循环顺序。
#
# Python3C + +Golang
#
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans
#
#
# 复杂度分析
#
# 时间复杂度：O(n ^ 2)
# O(n
# 2
# )，其中
# nn
# 是字符串的长度。动态规划的状态总数为
# O(n ^ 2)
# O(n
# 2
# )，对于每个状态，我们需要转移的时间为
# O(1)
# O(1)。
#
# 空间复杂度：O(n ^ 2)
# O(n
# 2
# )，即存储动态规划状态需要的空间。

