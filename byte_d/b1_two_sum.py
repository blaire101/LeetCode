# -*- coding: utf-8 -*-
"""
    @file: b1_two_sum.py
    @date: 2020-07-06 2:16 PM
    @https://leetcode-cn.com/company/bytedance/
"""

# [5, 5, 3, 9], 10

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(target - num)]
        hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


if __name__ == '__main__':
    pass
