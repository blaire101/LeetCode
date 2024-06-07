# -*- coding:utf-8 -*-

from typing import List

# 英文：Removing Duplicates from Sorted Arrays and Lists
# 中文：从排序数组和链表中删除重复元素
#
# LeetCode 常考点解释：
# 这两个问题在 LeetCode 上非常常见，通常以数组或链表的形式出现，需要移除重复元素并返回新数组或链表的长度或内容。
#
# 详细描述：
# Removing Elements Appearing More Than Once:
# 目标：从数组中移除出现超过一次的元素，只保留出现一次的元素。
# 示例：输入 [1, 1, 2, 3, 4, 4, 5]，输出 [2, 3, 5]。
# Removing Redundant Duplicates:
#
# 目标：从排序数组中移除冗余的重复元素，保留每个元素的一次出现。
# 示例：输入 [1, 1, 2, 3, 4, 4, 5]，输出 [1, 2, 3, 4, 5]。


class Solution:

    # 英文：Removing Duplicates from Sorted Arrays and Lists
    # 中文：从排序数组和链表中删除重复元素
    def remove_duplicates_elements_from_sort_array(self, nums: List[int]) -> List[int]:
        """
        Removes elements from a sorted list that appear more than once.
        Returns a new list containing only the elements that appear exactly once.

        :param nums: List[int] - A sorted list of integers which may contain duplicates
        :return: List[int] - A list of integers without elements that appear more than once
        """
        if not nums:
            return []

        unique_elements = []
        i = 0
        n = len(nums)

        while i < n:
            if (i == n - 1) or (nums[i] != nums[i + 1]):
                unique_elements.append(nums[i])
                i += 1
            else:
                while i < n - 1 and nums[i] == nums[i + 1]:
                    i += 2

        return unique_elements

    # 英文：Removing Duplicates from Sorted Arrays and Lists
    # 中文：从排序数组和链表中删除重复元素
    def remove_duplicates_elements_from_array(self, nums: List[int]) -> List[int]:
        """
        This function removes elements from the list that appear more than once.
        It returns a new list containing only the elements that appear exactly once.

        :param nums: List[int] - A list of integers which may contain duplicates
        :return: List[int] - A list of integers without elements that appear more than once
        """
        if not nums:
            return []

        unique_elements = []
        element_count = {}

        # Count occurrences of each element
        for num in nums:
            element_count[num] = element_count.get(num, 0) + 1

        # Collect elements that appear exactly once
        for num in nums:
            if element_count[num] == 1:
                unique_elements.append(num)

        return unique_elements

    # Removing Redundant Duplicates:
    # 目标：从排序数组中移除冗余的重复元素，保留每个元素的一次出现。
    # 示例：输入 [1, 1, 2, 3, 4, 4, 5]，输出 [1, 2, 3, 4, 5]。

    def remove_redundant_duplicates(self, nums: List[int]) -> List[int]:
        """
        This function removes redundant duplicates from a sorted list.
        It modifies the list in-place to keep only one occurrence of each element
        and returns the list with unique elements up to the new length.

        :param nums: List[int] - A sorted list of integers which may contain duplicates
        :return: List[int] - A list of integers with no redundant duplicates
        """
        if not nums:
            return []

        write_index = 1
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1
        # >>> a = [1,2,3,4,5]
        # >>> a[:3]  [1, 2, 3]
        return nums[:write_index]


if __name__ == '__main__':
    s = Solution()

    # Test remove_elements_appearing_more_than_once
    nums = [1, 1, 2, 3, 4, 4, 5]
    print("Elements appearing only once:", s.remove_duplicates_elements_from_sort_array(nums))

    print("Elements appearing only once:", s.remove_duplicates_elements_from_array(nums))

    # Test remove_redundant_duplicates
    nums = [1, 1, 2, 3, 4, 4, 5]
    print("Remove redundant duplicates:", s.remove_redundant_duplicates(nums))
