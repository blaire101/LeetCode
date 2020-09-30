# -*- coding: utf-8 -*-
"""
    @file: medium.rightSideView.py
    @date: 2020-09-25 7:47 AM
    @desc: 199. 二叉树的右视图
    @url : https://leetcode-cn.com/problems/binary-tree-right-side-view/
"""

# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# -*- coding: utf-8 -*-
"""
    @file: medium.rightSideView.py
    @date: 2020-09-25 7:47 AM
    @desc: 199. 二叉树的右视图
    @url : https://leetcode-cn.com/problems/binary-tree-right-side-view/
"""

# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = {}

        deq = deque()
        level = 1

        deq.append([root, level])
        while deq:
            cur_node, cur_level = deq.popleft()
            res[cur_level] = cur_node.val
            if cur_node.left:
                deq.append([cur_node.left, cur_level + 1])
            if cur_node.right:
                deq.append([cur_node.right, cur_level + 1])

        return [res[k] for k in res]
