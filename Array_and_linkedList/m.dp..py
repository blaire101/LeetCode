# -*- coding: utf-8 -*-
"""
    @file: m.dp..py
    @date: 2020-09-09 10:45 AM
    @desc: 剑指 Offer 60. n个骰子的点数
    @answ: https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/rong-yi-li-jie-de-pythondong-tai-gui-hua-fang-fa-b/
    @url : https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/
"""


# 解题思路
# 刚开始看着道题，大致思路是有，但是边界条件不是很好确定，看leetcode里面Python语言前面几个题解，看的不是很明白。
#
# 下面思路可能更容易理解。
# n个骰子，一共有6**n种情况
# n=1, 和为s的情况有 F(n,s)=1 s=1,2,3,4,5,6
# n>1 , F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)
# 可以看作是从前(n-1)个骰子投完之后的状态转移过来。
# 其中F（N,S）表示投第N个骰子时，点数和为S的次数
#
# 原文链接：https://blog.csdn.net/qq_24243877/article/details/104560944
#
# 代码
from typing import List


class Solution:
    def twoSum(self, n: int) -> List[float]:

        dp = [ [0 for _ in range(6*n+1)] for _ in range(n+1)]
        for i in range(1,7):
            dp[1][i] = 1

        for i in range(2,n+1):
            for j in range(i,i*6+1):
                for k in range(1,7):
                    if j >= k+1:
                        dp[i][j] +=dp[i-1][j-k]
        res = []
        for i in range(n,n*6+1):
            res.append(dp[n][i]*1.0/6**n)
        return res

#####动态规划
