# -*- coding: utf-8 -*-
"""
    @file: easy.getIntersectionNode.py
    @date: 2020-09-27 1:31 PM
    @desc: 160. 相交链表
    @url : https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        if (not headA and headB) or (not headB and headA):
            return None

        p1, p2 = headA, headB

        flag1, flag2 = 0, 0

        while p1 and p2:
            if p1 == p2:
                break

            if p1.next:
                p1 = p1.next
            else:
                if flag1 == 1:
                    return None
                p1 = headB
                flag1 = 1


            if p2.next:
                p2 = p2.next
            else:
                if flag2 == 1:
                    return None
                p2 = headA
                flag2 == 1


        return p1
