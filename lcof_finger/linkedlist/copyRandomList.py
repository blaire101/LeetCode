# -*- coding: utf-8 -*-
"""
    @file: copyRandomList.py
    @date: 2020-10-17 7:11 PM
    @desc: 剑指 Offer 35. 复杂链表的复制
    @url : https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        cur = head

        while cur:
            cur_copy = Node(cur.val, cur.next, cur.random)
            cur2 = cur.next

            cur.next = cur_copy
            cur_copy.next = cur2

            cur = cur2

        cur = head

        while cur:
            cur_post = cur.next

            if cur.random:
                cur_post.random = cur.random.next
            else:
                cur_post.random = None

            cur = cur.next.next

        cur = head
        new_head = cur.next

        while cur:
            cur_post = cur.next

            if cur_post.next:
                cur_post.next = cur_post.next.next

            cur = cur.next.next

        return new_head





