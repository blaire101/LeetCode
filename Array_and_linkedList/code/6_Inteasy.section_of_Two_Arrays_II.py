# -*- coding: utf-8 -*-
"""
    @file: 6_Intersection_of_Two_Arrays_II.py
    @date: 2019-12-22 16:46
"""
from typing import List


class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort(), nums2.sort()

        len1, len2 = len(nums1), len(nums2)

        i, j, res = 0, 0, []

        while i < len1 and j < len2:

            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i, j = i + 1, j + 1

            elif nums1[i] < nums2[j]:
                i += 1

            elif nums1[i] > nums2[j]:
                j += 1

        return res
