# -*- coding: utf-8 -*-
"""
    @file: 12-115.Distinct-Subsequences-I.py
    @date: 2020-09-05 5:21 PM
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        for arr in dp:
            print(arr)

        return dp[-1][-1]


if __name__ == '__main__':
    s = "rabbbit"
    t = 'rabbit'
    S = "babgbag"
    T = "bag"

    # dp[i][j] 代表 T 前 i 字符串可以由 S j 字符串组成最多个数.

    sol = Solution()

    res = sol.numDistinct(s=S, t=T)

    print(res)

    # dp[3][4]

# [1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 1, 1, 1, 1]
# [0, 0, 1, 1, 1, 1, 1, 1]
# [0, 0, 0, 1, 2, 3, 3, 3]
# [0, 0, 0, 0, 1, 3, 3, 3]
# [0, 0, 0, 0, 0, 0, 3, 3]
# [0, 0, 0, 0, 0, 0, 0, 3]
