# -*- coding: utf-8 -*-
"""
    @file: im.getLeastNumbers.py
    @date: 2020-09-08 10:23 AM
    @desc: 剑指 Offer 11. 旋转数组的最小数字
    @url : https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
"""

# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#
# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]

import heapq
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]

        heapq.heapify(hp)

        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])

        ans = [-x for x in hp]

        return ans


if __name__ == '__main__':

    sol = Solution()

    arr = [1, 20, 5, 3, 8, 6, 4, 100]

    ans = sol.getLeastNumbers(arr, 4)

    print(ans)

