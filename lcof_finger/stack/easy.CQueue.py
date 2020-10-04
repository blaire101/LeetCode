# -*- coding: utf-8 -*-
"""
    @file: easy.CQueue.py
    @date: 2020-10-02 10:40 AM
    @desc: 剑指 Offer 09. 用两个栈实现队列
    @url : https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
"""


class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()
