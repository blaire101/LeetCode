# -*- coding: utf-8 -*-
"""
    @file: ll-1.py
    @date: 2020-08-17 8:31 AM
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


# 1. head or del is null 2. del=head 3. del=tail 4. del=normal
def del_node(head, p_del):

    if head is None or p_del is None:
        return head

    if p_del == head:
        return head.next

    if p_del.next is None:
        tmp = head
        while tmp.next != p_del:
            tmp = tmp.next
        tmp.next = None

    else:
        p_del.val = p_del.next.val
        p_del.next = p_del.next.next

    return head