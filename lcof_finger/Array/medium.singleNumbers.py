# -*- coding: utf-8 -*-
"""
    @file: medium.singleNumbers.py
    @date: 2020-09-07 5:36 PM
    @desc: 剑指 Offer 56 - I. 数组中数字出现的次数
    @url : https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
"""

#一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)

# 示例 1：
#
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
# 示例 2：
#
# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]

import functools
from typing import List

# ret = functools.reduce(lambda x, y: x ^ y, nums)
# 意思就是对序列连续调用函数，如果不给初始值，则第一次调用传递


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for i in nums:
            if i & div:
                a ^= i
            else:
                b ^= i
        return [a, b]


if __name__ == '__main__':
    nums = [1, 2, 10, 4, 1, 4, 3, 3]

    nums = [1]
    sol = Solution()
    sol.singleNumbers(nums=nums)