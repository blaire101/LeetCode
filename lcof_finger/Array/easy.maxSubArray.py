# -*- coding: utf-8 -*-
"""
    @file: e.maxSubArray.py
    @date: 2020-09-07 2:45 PM
    @desc: 剑指 Offer 42. 连续子数组的最大和
    @url : https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
"""
from typing import List


# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

# [-3,-2,-2,-3], -2

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        dp = {}

        dp[0] = nums[0]

        for i in range(1, len(nums)):

            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]

        maxNum = dp[0]

        for i in range(1, len(dp)):
            if dp[i] > maxNum:
                maxNum = dp[i]

        return maxNum


if __name__ == '__main__':
    sol = Solution()
    maxNum = sol.maxSubArray(nums = [-3,-2,-2,-3])
    print(maxNum)
