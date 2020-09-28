# -*- coding: utf-8 -*-
"""
    @file: easy.twoSum.py
    @date: 2020-09-18 08:38 AM
    @desc: 两数之和
    @url : https://leetcode-cn.com/problems/two-sum/
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        for i, num in enumerate(nums):

            if hash.get(target-num) is not None:
                return [hash.get(target-num), i]

            hash[num] = i


if __name__ == '__main__':
    sol = Solution()
    res = sol.twoSum([2,5,7,9], 7)
    print(res)