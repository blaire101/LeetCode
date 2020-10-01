# -*- coding: utf-8 -*-
"""
    @file: medium.twoSum.py
    @date: 2020-09-13 8:33 AM
    @desc: 剑指 Offer 60. n个骰子的点数
    @answ: https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/nge-tou-zi-de-dian-shu-dong-tai-gui-hua-ji-qi-yo-3/
    @url : https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/
"""

# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
#
# 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
#
# 输入: 1
# 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
#
# 输入: 2
# 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]


# 通过题目我们知道一共投掷 n 枚骰子，那最后一个阶段很显然就是：当投掷完 n 枚骰子后，各个点数出现的次数。
#
# 注意，这里的点数指的是前 n 枚骰子的点数和，而不是第 n 枚骰子的点数，下文同理。
#
# 找出了最后一个阶段，那状态表示就简单了。
#
# 首先用数组的第一维来表示阶段，也就是投掷完了几枚骰子。
# 然后用第二维来表示投掷完这些骰子后，可能出现的点数。
# 数组的值就表示，该阶段各个点数出现的次数。
# 所以状态表示就是这样的：DP[i][j] ，表示投掷完 i 枚骰子后，点数 j 的出现次数。

# DP[i][j] += DP[i-1][j-cur];

from typing import List


class Solution:

    def twoSum(self, n: int) -> List[float]:

        dp = [[0] * (6 * n + 1) for _ in range(11 + 1)]  # 索引0不取，后面取到最大索引6*n

        for i in range(1, 7):  # init
            dp[1][i] = 1

        for i in range(2, n + 1):  # 从第二轮抛掷开始算
            for j in range(2, 6 * i + 1):  # 第二轮抛掷最小和为2，从大到小更新对应的抛掷次数
                # DP[j] = 0  # 每次投掷要从0更新dp[j]大小，点数和出现的次数要重新计算
                for cur in range(1, 7):  # 每次抛掷的点数
                    if j - cur <= 0:
                        break

                    if j - cur > (i - 1) * 6:
                        continue

                    dp[i][j] += dp[i - 1][j - cur]  # 根据上一轮来更新当前轮数据
                    print(f'{i}, {j}, ==== {i-1} {j-cur}')

        sum_ = 6 ** n
        res = []

        for i in range(n, 6 * n + 1):
            res.append(dp[n][i] * 1.0 / sum_)

        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.twoSum(7)
    print(res)