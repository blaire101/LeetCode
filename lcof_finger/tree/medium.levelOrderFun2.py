# -*- coding: utf-8 -*-
"""
    @file: medium.levelOrderFun1.py
    @date: 2020-10-11 5:31 PM
    @desc: 剑指 Offer 32 - III. 从上到下打印二叉树 III
    @url : https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
"""

from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append([root, 0])
        res = []
        tmp_dict = dict()
        while queue:
            cur, level = queue.popleft()
            if tmp_dict.get(level) is not None:
                tmp_dict[level].append(cur.val)
            else:
                tmp_dict[level] = [cur.val]

            if cur.left:
                queue.append([cur.left, level + 1])
            if cur.right:
                queue.append([cur.right, level + 1])

        for ix in range(len(tmp_dict)):
            if ix % 2 == 1:
                res.append(tmp_dict[ix][::-1])
            else:
                res.append(tmp_dict[ix])

        return res