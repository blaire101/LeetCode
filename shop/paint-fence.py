# -*- coding: utf-8 -*-
"""
    @type: dp
    @file: paint-fence.py
    @date: 2020-07-07 10:12 AM

    @desc: https://leetcode-cn.com/problems/paint-fence/
"""

# 有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，每个栅栏柱可以用其中一种颜色进行上色。
#
# 你需要给所有栅栏柱上色，并且保证其中相邻的栅栏柱 最多连续两个 颜色相同。然后，返回所有有效涂色的方案数。
#
# 注意:
# n 和 k 均为非负的整数。
#
# 示例:
#
# 输入: n = 3，k = 2
# 输出: 6
# 解析: 用 c1 表示颜色 1，c2 表示颜色 2，所有可能的涂色方案有:
#
#             柱 1    柱 2   柱 3
#  -----      -----  -----  -----
#    1         c1     c1     c2
#    2         c1     c2     c1
#    3         c1     c2     c2
#    4         c2     c1     c1 
#    5         c2     c1     c2
#    6         c2     c2     c1


# 当n=1时，有k种不同涂法
# 当n=2时，有k * k 种不同涂法（此时还不用考虑连续相邻两个相同的问题）
# 当n>2时：
# 设定paint(i), i>2 为第i张海报的涂法, 则我们需要考虑两种情况：
# 1. 如果和前一张海报涂色相同：则有paint(i-2) * (k-1)种涂法
# 2. 如果和梁遗址海报的涂色不同：则有paint(i-1) * (k-1)种涂法
# 所以DP的状态方程可以表示为:
# paint(i) = (paint(i-2)+paint(i-1))*(k-1)
# 用lru_cache代替了数组来存储DP状态，代码如下


from functools import lru_cache


def num_ways(n: int, k: int) -> int:
    if n == 0:
        return 0

    @lru_cache(None)
    def paint(i):
        if i == 2:
            return k * k
        if i == 1:
            return k
        return (paint(i - 2) + paint(i - 1)) * (k - 1)

    return paint(n)

# arr = []
# arr[1] = k, arr[2] = k*k