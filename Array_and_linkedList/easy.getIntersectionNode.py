# -*- coding: utf-8 -*-
"""
    @file: e.getIntersectionNode.py
    @date: 2020-09-07 11:32 AM
    @desc: 两个链表的第一个公共节点， 剑指 Offer 52.
    @answ: 浪漫相遇
    @url : https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1

#
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         lenA, lenB = 0, 0
#
#         p = headA
#         while p is not None:
#             lenA += 1
#             p = p.next
#
#         p = headB
#         while p is not None:
#             lenB += 1
#             p = p.next
#
#         firstStep = abs(lenA - lenB)
#         first, second = (headA, headB) if lenA >= lenB else (headB, headA)
#         cnt = 0
#
#         while cnt < firstStep:
#             first = first.next
#             cnt += 1
#
#         while first != second and first and second:
#             first = first.next
#             second = second.next
#
#         if first == second and first:
#             return first
#
#         return None




# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
# 本题与主站 160 题相同：https://leetcode-
