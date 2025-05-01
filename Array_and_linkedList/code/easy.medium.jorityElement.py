# -*- coding: utf-8 -*-
"""
    @file: e.majorityElement.py
    @date: 2020-09-07 8:41 AM
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if not nums:
            return None

        target = nums[0]
        cnt = 1

        for i in range(1, len(nums)):

            if cnt == 0:
                target = nums[i]
                cnt = 1
                continue

            if nums[i] != target:
                cnt -= 1
            else:
                cnt += 1

        return target
