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
 

#### 1.8 Merge Intervals & 1.9 Insert Interval

Problem: **Merge overlapping intervals**.
Sample :
- Input: [[1,3],[2,6],[8,10],[15,18]]
- Output: [[1,6],[8,10],[15,18]]  
Idea (Sort + One Pass): Sort by start; if current.start ≤ last.end → merge; else append.

Problem: **Insert overlapping intervals Then Merge**.

**Sample**  
- Input: `intervals = [[1,3],[6,9]]`, `newInterval = [2,5]`   --- Output: `[[1,5],[6,9]]`  
- Input: `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]`, `newInterval = [4,8]`  --- Output: `[[1,2],[3,10],[12,16]]`

**Idea (super easy to write):**  
Just append the new interval, sort by start, then do a single pass to merge overlaps (reuse the classic “merge intervals” logic).  
Time `O(n log n)` (due to sorting), code is tiny and reliable.

**Python (short & readable)**

```python
from typing import List

def insert_interval_easy(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    # 1) Put the new interval in
    intervals = intervals + [new_interval]
    # 2) Sort by start
    intervals.sort(key=lambda x: x[0])

    # 3) Merge in one pass
    merged: List[List[int]] = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            # no overlap → push
            merged.append([start, end])
        else:
            # overlap → extend the last interval's end
            merged[-1][1] = max(merged[-1][1], end)
    return merged

# Quick checks
print(insert_interval_easy([[1,3],[6,9]], [2,5]))                           # [[1,5],[6,9]]
print(insert_interval_easy([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))      # [[1,2],[3,10],[12,16]]
```


#### 1.10 Meeting Rooms I

Problem: Given intervals (meeting times), determine if a person can attend all meetings (no overlaps).

- Input: [[0,30],[5,10],[15,20]] → Output: False
- Input: [[7,10],[2,4]] → Output: True

```python
from typing import List
def can_attend_meetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True
# Examples
print(can_attend_meetings([[0,30],[5,10],[15,20]]))  # False
print(can_attend_meetings([[7,10],[2,4]]))           # True
```

#### 1.11 Meeting Rooms II - heapq.heappush(end_times, end)

Problem: Minimum number of conference rooms required given meeting intervals.

- Input: [[0,30],[5,10],[15,20]]
- Output：2

**Idea A — Min-Heap of end times (Greedy, O(n log n))**

1) Sort meetings by **start**.  
2) Keep a **min-heap** of current room **end times**.  
3) For each meeting:
   - If the **earliest ending** room `end <= start`, pop it (room freed) and reuse.
   - Push this meeting’s `end` time into heap (room occupied).
4) The **max heap size** reached is the answer.

**Python (Heap) — Readable & Annotated**

```python
from typing import List
import heapq

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Return the minimum number of conference rooms needed.
    intervals: List of [start, end], where 'end' is exclusive (standard LeetCode convention).
    """
    if not intervals:
        return 0
    # 1) Sort by start time
    intervals.sort(key=lambda itv: itv[0])
    # 2) Min-heap of end times for rooms currently in use
    end_times = []  # heap stores the 'end' time of each ongoing meeting

    for start, end in intervals:
        # If the earliest finishing room is free by 'start', reuse it
        if end_times and end_times[0] <= start:
            heapq.heappop(end_times)  # free that room

        # Assign (or reuse) a room for the current meeting until 'end'
        heapq.heappush(end_times, end)
    # Heap size equals the number of rooms needed at the peak
    return len(end_times)
```
    
#### Binary Search

- Binary Search
- Find First and Last Position of Element in Sorted Array

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
# Example (array must be sorted):
sorted_arr = [1, 2, 3, 5, 6, 8]
print("Binary Search index of 5:", binary_search(sorted_arr, 5))
```

**Find First and Last Position of Element in Sorted Array**

```python
from typing import List
def search_range(nums: List[int], target: int) -> List[int]:
    """
    Find the first and last index of target in sorted nums.
    If not found, return [-1, -1].
    """
    def find_bound(is_first: bool) -> int:
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1  # shrink left side
                else:
                    left = mid + 1   # shrink right side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound

    return [find_bound(True), find_bound(False)]

# Example
print(search_range([5,7,7,8,8,10], 8))   # [3, 4]
print(search_range([5,7,7,8,8,10], 6))   # [-1, -1]
```

**Merging Two Sorted Arrays**

```python
def merge_sorted(arr1, arr2):
    i = j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

# Example:
print("Merge Two Sorted Arrays:", merge_sorted([1, 3, 5], [2, 4, 6]))
```


#### Two Pointers
- 3Sum (two-pointers squeeze)
- Container With Most Water
- String to Integer (atoi)


**1) 3Sum (two-pointers squeeze)**

**Problem**  
Given an integer array `nums`, return all unique triplets `[a,b,c]` such that `a + b + c = 0`. Triplets must be unique (no duplicates).

**Sample**  
Input: `nums = [-1,0,1,2,-1,-4]`  
Output: `[[-1,-1,2],[-1,0,1]]`

**Idea**  
- Sort the array.  
- Fix index `i` (as `a`), then use two pointers `l` and `r` to find pairs (`b`,`c`) that sum to `-nums[i]`.  
- Skip duplicates for `i`, `l`, `r`.


```python
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res: List[List[int]] = []

    for i in range(n):
        # a) skip duplicate first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # b) two pointers for the remaining subarray
        target = -nums[i]
        l, r = i + 1, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                res.append([nums[i], nums[l], nums[r]])
                # move both pointers skipping duplicates
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                r -= 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
    return res
# Quick check
print(three_sum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
```

**Container With Most Water**

- Input: height = [1,8,6,2,5,4,8,3,7] Output: 49

**Idea (Two Pointers)**

```
Start with l=0, r=n-1. Area = (r - l) * min(height[l], height[r]).
```

| l | r | height\[l] | height\[r] | min | width | area | best | move |
| - | - | ---------- | ---------- | --- | ----- | ---- | ---- | ---- |
| 0 | 8 | 1          | 7          | 1   | 8     | 8    | 8    | l++  |
| 1 | 8 | 8          | 7          | 7   | 7     | 49   | 49   | r--  |
| 1 | 7 | 8          | 3          | 3   | 6     | 18   | 49   | r--  |
| 1 | 6 | 8          | 8          | 8   | 5     | 40   | 49   | r--  |
| 1 | 5 | 8          | 4          | 4   | 4     | 16   | 49   | r--  |
| … | … | …          | …          | …   | …     | …    | 49   | …    |

```python
from typing import List
def max_area(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        # Current container is limited by the shorter line
        h = min(height[l], height[r])
        width = r - l
        best = max(best, h * width)
        # Greedy move: discard the shorter side
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best
print(max_area([1,8,6,2,5,4,8,3,7]))  # 49
```

**String to Integer (atoi)**

```python
def myAtoi(s: str) -> int:
    s = s.lstrip()  # 1) remove leading spaces
    if not s:
        return 0
    
    # 2) check sign
    sign = 1
    i = 0
    if s[0] in ['-', '+']:
        sign = -1 if s[0] == '-' else 1
        i += 1
    
    # 3) read digits
    num = 0
    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1
    
    num *= sign
    
    # 4) clamp to 32-bit
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num

# Quick checks
print(myAtoi("42"))             # 42
print(myAtoi("   -42"))         # -42
print(myAtoi("4193 with words"))# 4193
print(myAtoi("words and 987"))  # 0
print(myAtoi("-91283472332"))   # -2147483648
```


#### Sliding Window
- Longest Substring Without Repeating Characters
- Continuous Sequence Sum Equals Target
- Sliding Window Maximum
- Minimum Window Substring

---

## Phase 2: Heap, Stack & Queue

- Kth Largest Element in an Array
- Find Smallest k Numbers (heapq)

#### 2.1 Kth Largest Element in an Array

```python
import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Example:
print("Kth Largest Element (k=2):", kth_largest([3, 2, 1, 5, 6, 4], 2))
```

#### 2.2 Find the Smallest k Numbers in an Array

```python
import heapq

def smallest_k(nums, k):
    return heapq.nsmallest(k, nums)

# Example:
print("Smallest k numbers (k=3):", smallest_k([3, 2, 1, 5, 6, 4], 3))
```


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


**Jump Game I & II → very high frequency, must-do.**
**Gas Station → high frequency, common greedy interview.**

🔹 1. Jump Game I (LeetCode 55)

Problem: Can you reach the last index?

```
Input: nums = [2,3,1,1,4]
Output: True   # can jump 0→1→4

Input: nums = [3,2,1,0,4]
Output: False  # stuck at index 3
```

```python
def canJump(nums):
    farthest = 0
    for i, step in enumerate(nums):
        if i > farthest:   
            return False
        farthest = max(farthest, i + step)
    return True
print(canJump([2,3,1,1,4]))  # True
print(canJump([3,2,1,0,4]))  # False
```

🔹 2. Jump Game II (LeetCode 45)

Problem: Minimum jumps to reach last index.

```
Input: nums = [2,3,1,1,4]
Output: 2   # jump 0→1→4

Input: nums = [1,2,1,1,1]
Output: 3   # jump 0→1→2→4
```

🔹 3. Gas Station (LeetCode 134)

Problem: Find start index if you can complete a full circle.

```
Input: gas  = [1,2,3,4,5]
       cost = [3,4,5,1,2]
Output: 3   # start at station 3 (index 3, gas=4)

Input: gas  = [2,3,4]
       cost = [3,4,3]
Output: -1  # impossible
```

```
from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    total, tank, start = 0, 0, 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:   # The current section cannot be continued, change the starting point
            start = i + 1
            tank = 0
    return start if total >= 0 else -1
```

### Phase 7: Backtracking
- Subsets
- Subsets II
- Permutations
- Permutations II
- Combination Sum
- Combination Sum II
- Palindrome Partitioning


