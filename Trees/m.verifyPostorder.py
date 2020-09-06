# -*- coding: utf-8 -*-
"""
    @file: m.verifyPostorder.py
    @date: 2020-09-06 6:58 PM
"""


class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j:
                return True

            p = i

            while postorder[p] < postorder[j]:
                p += 1

            m = p

            while postorder[p] > postorder[j]:
                p += 1

            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)

