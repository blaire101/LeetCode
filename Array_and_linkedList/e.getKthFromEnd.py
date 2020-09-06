# -*- coding: utf-8 -*-
"""
    @file: e.getKthFromEnd.py
    @date: 2020-09-06 10:18 PM
"""


# 给定一个链表: 1->2->3->4->5, 和 k = 2.
#
# 返回链表 4->5.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

        first, second = head, head

        for _ in range(k):
            first = first.next

        while first:
            first = first.next
            second = second.next

        return second
