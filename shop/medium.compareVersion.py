# -*- coding: utf-8 -*-
"""
    @file: medium.compareVersion.py
    @date: 2020-09-17 10:38 AM
    @desc: 165. 比较版本号
    @url : https://leetcode-cn.com/problems/compare-version-numbers/
"""

# 比较两个版本号 version1 和 version2。
# 如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。
#
# 你可以假设版本字符串非空，并且只包含数字和 . 字符。
#
#  . 字符不代表小数点，而是用于分隔数字序列。
#
# 例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。
#
# 你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
#  
#
# 示例 1:
#
# 输入: version1 = "0.1", version2 = "1.1"
# 输出: -1

# 示例 2:
#
# 输入: version1 = "1.0.1", version2 = "1"
# 输出: 1
# 示例 3:
#
# 输入: version1 = "7.5.2.4", version2 = "7.5.3"
# 输出: -1
# 示例 4：
#
# 输入：version1 = "1.01", version2 = "1.001"
# 输出：0
# 解释：忽略前导零，“01” 和 “001” 表示相同的数字 “1”。
# 示例 5：
#
# 输入：version1 = "1.0", version2 = "1.0.0"
# 输出：0
# 解释：version1 没有第三级修订号，这意味着它的第三级修订号默认为 “0”。
#  
#
# 提示：
#
# 版本字符串由以点 （.） 分隔的数字字符串组成。这个数字字符串可能有前导零。
# 版本字符串不以点开始或结束，并且其中不会有两个连续的点。


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if not version1 and not version2:
            return 0

        if not version1:
            return -1

        if not version2:
            return 1

        num_str_list1 = version1.split('.')
        num_str_list2 = version2.split('.')

        num_list1 = [0 if not num_str else int(num_str) for num_str in num_str_list1]

        num_list2 = [0 if not num_str else int(num_str) for num_str in num_str_list2]

        diff = abs(len(num_list1) - len(num_list2))

        if len(num_list1) > len(num_list2):
            num_list2 += diff * [0]
        else:
            num_list1 += diff * [0]

        i = 0
        while i < len(num_list1) and i < len(num_list2):
            if num_list1[i] < num_list2[i]:
                return -1
            elif num_list1[i] > num_list2[i]:
                return 1
            else:
                i += 1

        if len(num_list1) == len(num_list2):
            return 0

        if i == len(num_list1):
            return -1

        if i == len(num_list2):
            return 1


if __name__ == '__main__':
    sol = Solution()
    v1 = '1.0'
    v2 = '1.0.0'
    #     "1.0.0"
    res = sol.compareVersion(v1, v2)
    print(res)
