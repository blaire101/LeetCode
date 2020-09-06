# -*- coding: utf-8 -*-
"""
    @file: e.kthLargest.py
    @date: 2020-09-06 6:47 PM
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return

            dfs(root.right)
            if self.k == 0: return

            self.k -= 1

            if self.k == 0:
                self.res = root.val

            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res
