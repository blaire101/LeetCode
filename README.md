# 🌅 LeetCode Handbook 

## 1: Fundamentals 

### Arrays & Hashing

- Two Sum (HashMap)
- Maximum Subarray
- Product of Array Except Self


#### 1.1 Two Sum (HashMap)

Problem: Find indices of the two numbers such that they add up to the target.

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

Solution (HashMap / Dictionary)


```python
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i
    return []
```


#### 1.2 Maximum Subarray - DP

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6  --- 4,-1,2,1
```

> dp[i] = max(nums[i], dp[i-1] + nums[i])
> 
> dp[i] represents the maximum subarray ending with nums[i] 


```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n 
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])

        return max(dp)

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) 
```


```python
from typing import List

def max_subarray(nums: List[int]) -> int:
    curr = best = nums[0]
    for x in nums[1:]:
        curr = max(x, curr + x)
        best = max(best, curr)
    return best

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  
```


#### 1.3 Product of Array Except Self

Input: nums = [1, 2, 3, 4]  
Output: [24, 12, 8, 6] ✅


```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        answer = [1] * n
        
        # Left products
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        # Right products
        for i in range(n - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        # Final answer = left[i] * right[i]
        for i in range(n):
            answer[i] = left[i] * right[i]
        
        return answer

# Example
nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))  # [24, 12, 8, 6]

```

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Compute prefix products (left side)
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]   # Update left product for next index
        
        # Step 2: Multiply with suffix products (right side)
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]  # Update right product for next index
        
        return answer
```


### Arrays & Sorting

- Sort Array (Quick Sort, Merge Sort)
- Merge Sorted Array (two pointers, reverse order)
- Arrange Array to Minimum Number (cmp_to_key)
- Search Insert Position
- Spiral Matrix Printing
- Merge Intervals
- Insert Interval
- Meeting Rooms I
- Meeting Rooms II

#### 1.4 Quick Sort  left = [x for x in arr[1:] if x < pivot]

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
# Example:
print("Quick Sort:", quick_sort([3, 6, 2, 8, 1, 5]))
```

**1.5 Merge Sort** - recursion， append， extend

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# Example:
print("Merge Sort:", merge_sort([3, 6, 2, 8, 1, 5]))
```

#### 1.5 Arrange Array to Minimum Number (cmp_to_key)

**Sample**
- Input: `[3, 30, 34, 5, 9]`
- Output: `"3033459"`

**Idea (Greedy + Custom Sort):**
Sort numbers (as strings) by comparator on concatenations: `x+y < y+x` → `x` comes first. Edge case: all zeros → return `"0"`.

```python
from functools import cmp_to_key
from typing import List

def min_number(nums: List[int]) -> str:
    strs = list(map(str, nums))

    def cmp(a: str, b: str) -> int:
        if a + b < b + a: return -1
        if a + b > b + a: return 1
        return 0

    strs.sort(key=cmp_to_key(cmp))
    res = ''.join(strs).lstrip('0')
    return res or "0"
# Example
print(min_number([3, 30, 34, 5, 9]))  # "3033459"
```

#### 1.6 Search Insert Position - Binary Search lower_bound

Problem: Return the index if the target is found; otherwise, return the index where it would be inserted in order.

```
Input: nums = [1,3,5,6], target = 5 → Output: 2
Input: nums = [1,3,5,6], target = 2 → Output: 1
```

Idea (Binary Search): Standard lower_bound.

```python
from typing import List

def search_insert(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l

# Examples
print(search_insert([1,3,5,6], 5))  # 2
print(search_insert([1,3,5,6], 2))  # 1
```

#### 1.7 Spiral Matrix Printing

<details>
<summary><strong>Spiral Matrix Printing</strong></summary>

```
Input:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

Idea (Layer-by-layer): Keep boundaries top, bottom, left, right and peel the matrix in rounds.

```python
from typing import List
def spiral_order(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1): res.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1): res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1): res.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1): res.append(matrix[i][left])
            left += 1
    return res
print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,3,6,9,8,7,4,5]
```

</details>
 
- Merge Intervals

Problem: Merge overlapping intervals.
Sample :
- Input: [[1,3],[2,6],[8,10],[15,18]]
- Output: [[1,6],[8,10],[15,18]]  
Idea (Sort + One Pass): Sort by start; if current.start ≤ last.end → merge; else append.

```python
from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    # If no intervals, return empty list
    if not intervals:
        return []
    
    # Sort intervals by their start time
    intervals.sort(key=lambda interval: interval[0])
    
    # Initialize the merged list with the first interval
    merged_intervals = [intervals[0]]
    
    # Iterate through the rest of the intervals
    for current_start, current_end in intervals[1:]:
        last_start, last_end = merged_intervals[-1]  # get the last merged interval
        
        # Check if the current interval overlaps with the last one
        if current_start <= last_end:
            # Merge them by extending the end
            merged_intervals[-1][1] = max(last_end, current_end)
        else:
            # Otherwise, no overlap → append as a new interval
            merged_intervals.append([current_start, current_end])
    
    return merged_intervals

# Example
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  
# [[1,6],[8,10],[15,18]]
```

- Insert Interval
- Meeting Rooms I
- Meeting Rooms II



#### Binary Search
- Binary Search
- Find First and Last Position of Element in Sorted Array

#### Two Pointers
- 3Sum (two-pointers squeeze)
- Container With Most Water
- String to Integer (atoi)

#### Sliding Window
- Longest Substring Without Repeating Characters
- Continuous Sequence Sum Equals Target
- Sliding Window Maximum
- Minimum Window Substring

---

### Phase 2: Heap, Stack & Queue
#### Heap
- Kth Largest Element in an Array
- Find Smallest k Numbers (heapq)

#### Stack & Queue
- Valid Parentheses
- Min Stack
- Implement Queue using Stacks
- Daily Temperatures
- Decode String (“3[a2[c]]”)
- LRU Cache
- Flatten Nested List Iterator

---

### Phase 3: Linked List
- Merge Two Sorted Lists
- Reverse Linked List
- Reverse Linked List II
- Remove Duplicates from Sorted List II
- Partition List
- Rotate Linked List
- Linked List Addition (e.g., 617 + 295)
- Linked List Cycle
- Linked List Cycle II
- Palindrome Linked List

---

### Phase 4: Dynamic Programming
#### Basics
- Climbing Stairs
- House Robber
- Longest Increasing Subsequence
- Coin Change

#### Grid / Paths
- Unique Paths
- Unique Paths II
- Minimum Path Sum

#### Stocks
- Best Time to Buy and Sell Stock I
- Best Time to Buy and Sell Stock II
- Best Time to Buy and Sell Stock with Cooldown
- Best Time to Buy and Sell Stock with Fee
- Best Time to Buy and Sell Stock III

#### Strings
- Longest Palindromic Substring
- Edit Distance
- Longest Common Subsequence
- Word Break

---

### Phase 5: DFS / BFS
- Word Search in Matrix
- Robot Movement Range (BFS)
- Number of Islands
- Course Schedule
- Course Schedule II
- Word Ladder
- Clone Graph
- Network Delay Time

---

### Phase 6: Greedy
- Jump Game I
- Jump Game II
- Gas Station
- Assign Cookies

---

### Phase 7: Backtracking
- Subsets
- Subsets II
- Permutations
- Permutations II
- Combination Sum
- Combination Sum II
- Palindrome Partitioning

---

### Phase 8: Trie & Advanced Strings
- Implement Trie (Prefix Tree)
- Word Search II
- Add and Search Word (Trie + Regex)
- Word Break II
