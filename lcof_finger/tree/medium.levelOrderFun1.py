# -*- coding: utf-8 -*-
"""
    @file: medium.levelOrderFun1.py
    @date: 2020-10-11 5:31 PM
    @desc: 剑指 Offer 32 - III. 从上到下打印二叉树 III
    @url : https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []
        cnt = 0
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if level:
                if cnt % 2 == 0:
                    res.append(level)
                else:
                    res.append(level[::-1])
                cnt += 1
        return res