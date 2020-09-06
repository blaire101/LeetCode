# -*- coding: utf-8 -*-
"""
    @file: lowestCommonAncestor.py
    @date: 2020-09-06 6:44 PM
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 当越过叶节点，则直接返回 null
        # 当 rootroot 等于 p, q， 则直接返回 root
        if root == None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right: return None

        if not left: return right
        if not right: return left

        return root
        # if left != None and right != None:
        #    return root