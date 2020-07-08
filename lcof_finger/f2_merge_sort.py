# -*- coding: utf-8 -*-
"""
    @file: f2_merge_sort.py
    @date: 2020-07-06 12:03 PM
"""

from typing import List


class Solution:

    def reverse_pairs(self, nums: List[int]) -> int:

        self.cnt = 0

        '''
        8, 5, 4, 9, 2, 3, 6
        '''

        def merge(nums, start, mid, end, temp):
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.cnt += mid - i + 1
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1

            for i in range(len(temp)):
                nums[start + i] = temp[i]

            temp.clear()

        def merge_sort(nums, start, end, temp):
            if start >= end:
                return
            mid = (start + end) >> 1
            merge_sort(nums, start, mid, temp)
            merge_sort(nums, mid + 1, end, temp)
            merge(nums, start, mid, end, temp)

        merge_sort(nums, 0, len(nums) - 1, [])

        return self.cnt


# 时间复杂度：O(NlogN)O(NlogN)
# 空间复杂度：O(N)O(N)

if __name__ == '__main__':
    s = Solution()

    nums = [8, 5, 4, 9, 2, 3, 6]

    cnt = s.reverse_pairs(nums)

    print(cnt)
