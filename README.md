# [LC][0]

📩 To the one with a hammer, everything looks like a nail.

# Easy Collection

# [1. top-interview-questions-easy][1]

## [1. Array][Array]

 1. Remove Duplicates from Sorted Array 
 2. Best Time to Buy and Sell Stock II
 3. Rotate Array
 4. Contains Duplicate
 5. Single Number
 6. Intersection of Two Arrays II
 7. Plus One
 8. Move Zeroes
 9. Two Sum
 10. Valid Sudoku
 11. Rotate Image
 
## 1.1 Remove Duplicates from Sorted Array

```python
def remove_duplicates_elements_from_sort_array(self, nums: List[int]) -> List[int]:
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
```
 
## 1.2 Best Time to Buy and Sell Stock II - Greedy Algorithm

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
``` 
  
## 1.3 Rotate Array - reverse3times

```python
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle cases where k >= n

        # Step 1: Reverse the entire array
        self.reverse(nums, 0, n - 1)
        # Step 2: Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        # Step 3: Reverse the remaining elements
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """
        Helper function to reverse elements from start to end.
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
```

## 1.4 Contains Duplicate




  
## 1.5 Single Number - XOR

```python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single
```

**XOR (exclusive OR)** is a bitwise operation that operates as follows:
- It returns 0 if both bits are the same.
- It returns 1 if the bits are different.

**Rules:**
- 0 ^ 0 = 0
- 1 ^ 1 = 0
- 0 ^ 1 = 1
- 1 ^ 0 = 1
  
## Reference

- [初级算法 • 数组](https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/)

[0]: https://leetcode.com/
[1]: https://leetcode.com/explore/interview/card/top-interview-questions-easy/

[Array]: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/
[1.1]: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
[1.2]: https://leetcode-cn.com/articles/best-time-to-buy-and-sell-stock-ii/
