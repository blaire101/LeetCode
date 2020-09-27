# -*- coding: utf-8 -*-
"""
    @file: medium.inorderTraversal.py
    @date: 2020-09-27 3:49 PM
    @desc: 94. 二叉树的中序遍历
    @url : https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = list()

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            self.res.append(root.val)

            root = root.right

        return self.res