# -*- coding: utf-8 -*-
"""
    @file: easy.addStrings.py
    @date: 2020-09-28 4:02 PM
    @desc: 415. 字符串相加
    @url : https://leetcode-cn.com/problems/add-strings/
"""


# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
#  
#
# 提示：
#
# num1 和num2 的长度都小于 5100
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        num1 = "".join(list(reversed(num1)))
        num2 = "".join(list(reversed(num2)))

        diff2 = len(num1) - len(num2)

        diff1 = diff2 * -1

        num1 = num1 + ("0" * diff1)
        num2 = num2 + ("0" * diff2)

        res = ""
        carry = 0

        for i in range(len(num1)):
            d1 = int(num1[i])
            d2 = int(num2[i])

            tmp = carry + d1 + d2
            res += str(tmp % 10)

            carry = tmp // 10

        if carry > 0:
            res += str(carry % 10)

        return "".join(list(reversed(res)))


if __name__ == '__main__':
    sol = Solution()
    res = sol.addStrings("1", "1")
    print(res)
