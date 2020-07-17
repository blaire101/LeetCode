# -*- coding: utf-8 -*-
"""
    @file: s7_str_decode.py
    @date: 2020-07-16 10:18 AM
    @desc: https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
"""


# 示例 1：
#
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
# 示例 2：
#
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
# 示例 3：
#
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
# 示例 4：
#
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"



# 解法一：辅助栈法
# 本题难点在于括号内嵌套括号，需要从内向外生成与拼接字符串，这与栈的先入后出特性对应。


class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

# 解法二：递归法
# 总体思路与辅助栈法一致，不同点在于将 [ 和 ] 分别作为递归的开启与终止条件：
#
# 当 s[i] == ']' 时，返回当前括号内记录的 res 字符串与 ] 的索引 i （更新上层递归指针位置）；
# 当 s[i] == '[' 时，开启新一层递归，记录此 [...] 内字符串 tmp 和递归后的最新索引 i，并执行 res + multi * tmp 拼接字符串。
# 遍历完毕后返回 res。
# 复杂度分析：
#
# 时间复杂度 O(N)O(N)，递归会更新索引，因此实际上还是一次遍历 s；
# 空间复杂度 O(N)O(N)，极端情况下递归深度将会达到线性级别。

# class Solution:
#     def decodeString(self, s: str) -> str:
#         def dfs(s, i):
#             res, multi = "", 0
#             while i < len(s):
#                 if '0' <= s[i] <= '9':
#                     multi = multi * 10 + int(s[i])
#                 elif s[i] == '[':
#                     i, tmp = dfs(s, i + 1)
#                     res += multi * tmp
#                     multi = 0
#                 elif s[i] == ']':
#                     return i, res
#                 else:
#                     res += s[i]
#                 i += 1
#             return res
#         return dfs(s,0)

