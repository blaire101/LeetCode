# -*- coding: utf-8 -*-
"""
    @file: medium.buildTree.py
    @date: 2020-09-28 3:03 PM
    @desc: 105. 从前序与中序遍历序列构造二叉树
    @url : https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pass
