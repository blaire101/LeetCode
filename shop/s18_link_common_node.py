# -*- coding: utf-8 -*-
"""
    @file: s18_link_common_node.py
    @date: 2020-07-27 11:22 AM
"""


# https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 图解 双指针法，浪漫相遇
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    node1, node2 = headA, headB

    while node1 != node2:
        node1 = node1.next if node1 else headB
        node2 = node2.next if node2 else headA

    return node1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         temphead = headA
#         lenA = 0
#         while temphead:
#             temphead = temphead.next
#             lenA += 1
#         temphead = headB
#         lenB = 0
#         while temphead:
#             temphead = temphead.next
#             lenB += 1
#         dLen = abs(lenA - lenB)
#         if lenA - lenB >= 0:
#             # 分别表示较长的链表和较短的链表
#             headl, heads = headA, headB
#         else:
#             headl, heads = headB, headA
#         while dLen > 0:
#             headl = headl.next
#             dLen -= 1
#         while headl and heads:
#             if headl == heads:
#                 return headl
#             headl = headl.next
#             heads = heads.next
#         return None

if __name__ == '__main__':
    print("hello")
