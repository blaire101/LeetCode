# -*- coding: utf-8 -*-
"""
    @file: e.reverseLinkedList.py
    @date: 2020-09-06 10:41 PM
"""


# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head) -> ListNode:
        if (head == None or head.next == None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur


if __name__ == '__main__':
    pass
