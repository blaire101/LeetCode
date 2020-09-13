# -*- coding: utf-8 -*-
"""
    @file: e.ti-huan-kong-ge-lcof.py
    @date: 2020-09-06 10:12 PM
"""


# 输入：s = "We are happy."
# 输出："We%20are%20happy."


class Solution:
    def replaceSpace(self, s: str) -> str:
        s = s.replace(" ", "%20")
        return s


if __name__ == '__main__':
    pass
