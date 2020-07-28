# -*- coding: utf-8 -*-
"""
    @file: s22-del-link-reverse.py
    @date: 2020-07-29 10:15 AM
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        slownode = ListNode(None)
        slownode.next = head
        fastnode = slownode
        for i in range(n):
            fastnode = fastnode.next
        while (fastnode.next != None):
            slownode = slownode.next
            fastnode = fastnode.next
        if slownode.next == head:
            head = head.next
        else:
            slownode.next = slownode.next.next
        return head
