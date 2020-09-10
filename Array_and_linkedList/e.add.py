# -*- coding: utf-8 -*-
"""
    @file: e.add.py
    @date: 2020-09-10 10:19 AM
    @desc: 剑指 Offer 65. 不用加减乘除做加法
    @url : https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/
    @answ: https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/
"""

# class Solution {
#     public int add(int a, int b) {
#         while(b != 0) { // 当进位为 0 时跳出
#             int c = (a & b) << 1;  // c = 进位
#             a ^= b; // a = 非进位和
#             b = c; // b = 进位
#         }
#         return a;
#     }
# }


class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

