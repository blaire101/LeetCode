# -*- coding: utf-8 -*-
"""
    @file: e.reversePrintLinkedList.py
    @date: 2020-09-06 10:36 PM
"""

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None:
            return []

        return self.reversePrint(head.next) + [head.val]