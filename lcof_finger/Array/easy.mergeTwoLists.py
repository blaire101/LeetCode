# -*- coding: utf-8 -*-
"""
    @file: easy.mergeTwoLists.py
    @date: 2020-10-02 10:52 AM
    @desc:
    @url : 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            p = ListNode(l1.val)
            p.next = self.mergeTwoLists(l1.next, l2)
        else:
            p = ListNode(l2.val)
            p.next = self.mergeTwoLists(l1, l2.next)

        return p