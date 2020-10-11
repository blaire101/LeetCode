# -*- coding: utf-8 -*-
"""
    @file: medium.validateStackSequences.py
    @date: 2020-10-11 2:21 PM
    @desc: 剑指 Offer 31. 栈的压入、弹出序列
    @url : https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
"""

# 示例 1：
#
# 输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# 示例 2：
#
# 输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# 输出：false
# 解释：1 不能在 2 之前弹出

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)
            if i == popped[j]:
                j += 1
                stack.pop()

            while stack:
                if stack[-1] == popped[j]:
                    j += 1
                    stack.pop()
                else:
                    break

        return len(stack) == 0


if __name__ == '__main__':
    pass