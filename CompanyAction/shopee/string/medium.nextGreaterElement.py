# -*- coding: utf-8 -*-
"""
    @file: medium.nextGreaterElement.py
    @desc: 556. 下一个更大元素 III
    @date: 2020-07-08 11:21 AM
    @answ: https://leetcode-cn.com/problems/next-greater-element-iii/solution/xia-yi-ge-geng-da-yuan-su-iii-by-leetcode/
    @url : https://leetcode-cn.com/problems/next-greater-element-iii/
"""


# 1 5 8 4 7 6 5 3 1
#
# 1 5 8 5 7 6 4 3 1
#
# 1 5 8 5 1 3 4 6 7


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_list = [i for i in str(n)]
        length = len(str_list)
        end = length - 1
        max_val = '-1'

        def swap(i, j):
            temp = str_list[i]
            str_list[i] = str_list[j]
            str_list[j] = temp

        while end >= 0 and str_list[end] >= max_val:
            max_val = str_list[end]
            end = end - 1

        if end == -1:
            return -1

        i = end + 1
        j = length - 1

        while i <= j:
            swap(i, j)
            i = i + 1
            j = j - 1

        i = end + 1
        # 7
        print(str_list)
        while i < length:
            if str_list[i] > str_list[end]:
                swap(i, end)
                break
            else:
                i = i + 1

        result = int("".join(str_list))
        if result > 2147483647:
            return -1
        else:
            return result


if __name__ == '__main__':
    sol = Solution()
    n = 158476531
    sol.nextGreaterElement(n=n)
