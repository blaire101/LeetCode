# -*- coding: utf-8 -*-
"""
    @file: hard.isMatch.py
    @date: 2020-09-12 1:04 PM
    @desc: 剑指 Offer 19. 正则表达式匹配
    @answ: https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/hui-su-dong-tai-gui-hua-by-ml-zimingmeng/
    @url : https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/
"""

import re

# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。

# 转移方程
# f[i][j] 代表 A 的前 i 个和 B 的前 j 个能否匹配
#
# 对于前面两个情况，可以合并成一种情况
#
# f[i][j] = f[i-1][j-1]
#
# 对于第三种情况，对于 c* 分为看和不看两种情况
#
# 不看：直接砍掉正则串的后面两个， f[i][j] = f[i][j-2]
# 看：正则串不动，主串前移一个，f[i][j] = f[i-1][j]
# 初始条件
# 特判：需要考虑空串空正则
#
# 空串和空正则是匹配的，f[0][0] = true
# 空串和非空正则，不能直接定义 true 和 false，必须要计算出来。（比如A= '' ,B=a∗b∗c∗）
# 非空串和空正则必不匹配，f[1][0]=...=f[n][0]=false
# 非空串和非空正则，那肯定是需要计算的了。
#

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         ans = re.fullmatch(p, s)
#         return ans != None


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 边界条件，考虑 s 或 p 分别为空的情况
        if not p: return not s
        if not s and len(p) == 1: return False

        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        # 初始状态
        dp[0][0] = True
        dp[0][1] = False

        for c in range(2, n):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]

        for r in range(1, m):
            i = r - 1
            for c in range(1, n):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':  # ‘*’前面的字符匹配s[i] 或者为'.'
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:  # ‘*’匹配了0次前面的字符
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    a = {1, "ab"}
    print(type(a))

