# -*- coding:utf-8 -*-

# Topic: Remove Duplicates from Sorted Array

import sys
from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: list[int]
        :rtype: int
        """

        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
            else:
                i = i + 1

        return len(nums)


if __name__ == '__main__':
    print(sys.version)
    # print(sys.version_info)

    s = Solution()

    new_len = s.removeDuplicates([1, 1, 2])

    print(new_len)
