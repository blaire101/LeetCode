# -*- coding: utf-8 -*-
"""
    @file: lowestCommonAncestor.py
    @date: 2020-09-11 6:44 PM
    @desc: 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
    @url : https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 算法:
# 1. 从根节点开始遍历树
# 2. 如果节点 p 和节点 q 都在右子树上，那么以右孩子为根节点继续 1 的操作
# 3. 如果节点 p 和节点 q 都在左子树上，那么以左孩子为根节点继续 1 的操作
# 4. 如果条件 2 和条件 3 都不成立，这就意味着我们已经找到节 p 和节点 q 的 LCA 了

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Value of current node or parent node.
        parent_val = root.val
        # Value of p
        p_val = p.val
        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root