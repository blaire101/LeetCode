# -*- coding: utf-8 -*-
"""
    @file: medium.removeNthFromEnd.py
    @date: 2020-09-23 10:44 AM
    @desc: 19. 删除链表的倒数第N个节点
    @url : https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
# when you submit this code, please comment this class ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# [1] 1
# pre is None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        pre, post = head, head

        for i in range(n):
            pre = pre.next

        if pre is None:
            return head.next

        while pre.next is not None:
            pre = pre.next
            post = post.next

        post.next = post.next.next

        return head
