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
 
## 1.2 Best Time to Buy and Sell Stock II

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
  
  
  
## Reference

- [初级算法 • 数组](https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/)

[0]: https://leetcode.com/
[1]: https://leetcode.com/explore/interview/card/top-interview-questions-easy/

[Array]: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/
[1.1]: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
[1.2]: https://leetcode-cn.com/articles/best-time-to-buy-and-sell-stock-ii/
