# -*- coding: utf-8 -*-
"""
    @file: medium.permutation.py
    @date: 2020-10-02 3:43 PM
    @desc: 剑指 Offer 38. 字符串的排列
    @answ: https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/
    @url : https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
"""

# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]

from typing import List


class Solution:

    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []

        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))  # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue  # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)  # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换

        dfs(0)
        return res
