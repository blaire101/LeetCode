# -*- coding: utf-8 -*-
"""
    @file: f8_topK.py
    @date: 2020-07-13 11:17 AM
"""


# 2. partition方法(基于快速排序)
#
#
# 这个其实就是快速排序的思想了,我们要找其中 K 个最小的元素,而快速排序则是没一回合都根据基础数分成两个部分,左边的小于基础数,右面的大于基础数.
# 根据这个思想我们可以找每次排序完,如果基础数的坐标 i 恰好等于 k ,那么我们就可以确定 arr[:k]就是我们的解


class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 方法一:partition方法(基于快速排序)
        if k > len(arr) or k <= 0:
            return []
        start = 0
        end = len(arr) - 1
        index = self.quickSort(arr, start, end)
        while index != k - 1:
            print(index)
            if index > k - 1:
                end = index - 1
                index = self.quickSort(arr, start, end)
            if index < k - 1:
                start = index + 1
                index = self.quickSort(arr, start, end)
        return arr[:k]

    def quickSort(self, arr, start, end):
        low = start
        high = end
        temp = arr[start]
        while low < high:
            while low < high and arr[high] >= temp:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] < temp:
                low += 1
            arr[high] = arr[low]
        arr[low] = temp
        return low

# void quickSort(int a[], int left, int right) {
#     if(left < right) { // exit. good idea!
#         int l = left, r = right, x = a[l];
#         while(1) {
#             while(l < r && a[r] >= x) r--;
#             while(l < r && a[l] <= x) l++;
#             if(l >= r) break;
#             swap(a[r], a[l]);
#         }
#         swap(a[left], a[l]);
#         quickSort(a, left, l-1);
#         quickSort(a, l+1, right);
#     }
# }
