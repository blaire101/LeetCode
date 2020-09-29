# -*- coding: utf-8 -*-
"""
    @file: knowledge.binarySearch.py
    @date: 2020-09-17 10:04 AM
    @url : https://segmentfault.com/a/1190000008699980
"""

# /* 注意：题目保证数组不为空，且 n 大于等于 1 ，以下问题默认相同 */
# int BinarySearch(int array[], int n, int value)
# {
#     int left = 0;
#     int right = n - 1;
#     // 如果这里是 int right = n 的话，那么下面有两处地方需要修改，以保证一一对应：
#     // 1、下面循环的条件则是 while(left < right)
#     // 2、循环内当 array[middle] > value 的时候，right = middle
#
#     while (left <= right)  // 循环条件，适时而变
#     {
#         int middle = left + ((right - left) >> 1);  // 防止溢出，移位也更高效。同时，每次循环都需要更新。
#         if (array[middle] > value)
#             right = middle - 1;
#         else if (array[middle] < value)
#             left = middle + 1;
#         else
#             return middle;
#     }
#
#     return -1;
# }

# 给定一个有序的数组，查找第一个等于 value 的下标，找不到返回 -1。
# 例如：{ 1, 2, 2, 2, 4 } 找 2，返回下标 1（下标从 0 开始计算）。

# int BinarySearch(int array[], int n, int value)
# {
#     int left = 0;
#     int right = n - 1;
#
#     while (left <= right)
#     {
#         int middle = left + ((right - left) >> 1);
#
#         if (array[middle] >= value)  // 因为是找到最小的等值下标，所以等号放在这里
#             right = middle - 1;
#         else
#             left = middle + 1;
#     }
#
#     if (left < n && array[left] == value)
#         return left;
#
#     return -1;
# }