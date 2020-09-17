# -*- coding: utf-8 -*-
"""
    @file: very hard.super-egg-drop.py
    @date: 2020-09-17 10:12 AM
    @url : https://leetcode-cn.com/problems/super-egg-drop/
"""

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}
        def dp(k, n):
            # print(k, n)
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k-1, x-1)
                        t2 = dp(k, n-x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x
                    # print(lo, hi)
                    ans = 1 + min(max(dp(k-1, x-1), dp(k, n-x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(K, N)


if __name__ == '__main__':
    sol = Solution()
    res = sol.superEggDrop(2, 100)
    print(res)
