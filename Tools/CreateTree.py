# -*- coding: utf-8 -*-
"""
    @file: CreateTree.py
    @date: 2020-10-11 1:05 PM
"""

from collections import deque


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def creatTree(vals):

    nodes = []

    for i in range(len(vals)):

        cur_val = vals[i]
        if cur_val is not None:
            cur_node = Node(cur_val)
        else:
            cur_node = None

        nodes.append(cur_node)

        if i > 0:
            # 0, 1-1/2, 2-1/2
            par_id = (i - 1) // 2
            if (i - 1) % 2 == 0:
                nodes[par_id].left = cur_node
            else:
                nodes[par_id].right = cur_node


    return nodes[0]


def pre_out(root):
    if not root:
        return None

    print(root.val)
    pre_out(root.left)
    pre_out(root.right)


if __name__ == '__main__':

    vals = [3,5,1,6,2,0,8,None,None,7,4]

    root = creatTree(vals)

    pre_out(root)
