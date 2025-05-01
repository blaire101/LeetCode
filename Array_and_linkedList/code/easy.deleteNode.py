# -*- coding: utf-8 -*-
"""
    @file: e.deleteNode
    @date: 2020-09-11 8:44 PM
    @desc: 剑指 Offer 18. 删除链表的节点
    @url : https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        if head.val == val:
            return head.next
        pre, p = head, head.next

        while p:
            if p.val == val:
                pre.next = p.next
                return head

            p = p.next
            pre = pre.next

        return head
