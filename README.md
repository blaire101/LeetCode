# 🌅 LeetCode Handbook 

## 📚 Table of Contents

- [Phase 1: Fundamentals ](#phase-1-fundamentals-1)
- [Phase 2: Heap, Stack & Queue](#phase-2-heap-stack--queue-1)
- [Phase 3: Linked List](#phase-3-linked-list)
- [Phase 4: Dynamic Programming](#phase-4-dynamic-programming)
- [Phase 5: DFS / BFS](#phase-5-dfs--bfs)
- [Phase 6: Greedy](#phase-6-greedy)
- [Phase 7: Backtracking](#phase-7-backtracking)

## Phase 1: Fundamentals 
	
### Arrays & Hashing
- Two Sum (1) - HF  
- Maximum Subarray / Kadane (53) - HF  
- Product of Array Except Self (238) - HF  
	
### Arrays & Sorting
- Sort Array (912, Quick Sort / Merge Sort)  
- Merge Sorted Array (88)    **append, pop, extend**
- Arrange Array to Minimum Number (剑指 Offer)  
- Search Insert Position (35)  
- Merge Intervals (56) - HF  
- Insert Interval (57) - HF  
- Meeting Rooms I (252)  
- Meeting Rooms II (253) - HF  
	
### Binary Search
- Binary Search (704) - HF  
- Find First and Last Position of Element in Sorted Array (34) - HF  
	
### Two Pointers
- 3Sum (15) - HF  
- Container With Most Water (11) - HF  
- String to Integer (8, atoi)  
	
### Sliding Window
- Longest Substring Without Repeating Characters (3 / Offer 48) - HF  
- Continuous Sequence Sum Equals Target (剑指 Offer)  
- Sliding Window Maximum (239) - HF  
- Minimum Window Substring (76) - HF  

## Phase 2: Heap, Stack & Queue

### Heap
- Kth Largest Element in an Array (215) - HF  
- Find Smallest k Numbers (剑指 Offer)  

### Stack & Queue
- Valid Parentheses (20) - HF  
- Implement Queue using Stacks (232)  
- Daily Temperatures (739) - HF  
- Decode String (394)  
- LRU Cache (146) - HF  
- Flatten Nested List Iterator (341)  


## Phase 3: Linked List
- Merge Two Sorted Lists (21) - HF  
- Reverse Linked List (206) - HF  
- Remove Duplicates from Sorted List II (82)  
- Linked List Cycle (141) - HF  


## Phase 4: Dynamic Programming

### Basics
- Climbing Stairs (70) - HF  
- House Robber (198) - HF  
- Longest Increasing Subsequence (300)  
- Coin Change (322) - HF  

### Grid / Paths
- Unique Paths (62) - HF  
- Unique Paths II (63)  
- Minimum Path Sum (64) - HF  

### Stocks
- Best Time to Buy and Sell Stock I (121) - HF  
- Best Time to Buy and Sell Stock II (122) - HF  
- Best Time to Buy and Sell Stock with Cooldown (309)  
- Best Time to Buy and Sell Stock with Fee (714)  
- Best Time to Buy and Sell Stock III (123)  

### Strings
- Longest Palindromic Substring (5)  
- Edit Distance (72) - HF  
- Longest Common Subsequence (1143)  
- Word Break (139) - HF  

## Phase 5: DFS / BFS
- Word Search in Matrix (79) - HF  
- Robot Movement Range (Offer 13)  
- Number of Islands (200) - HF  
- Course Schedule (207) - HF  
- Course Schedule II (210)  
- Word Ladder (127) - HF  
- Clone Graph (133)  
- Network Delay Time (743)  

## Phase 6: Greedy
- Jump Game I (55) - HF  
- Jump Game II (45) - HF  
- Gas Station (134) - HF  


## Phase 7: Backtracking
- Subsets (78) - HF  
- Subsets II (90) - HF  
- Permutations (46) - HF  
- Permutations II (47)  
- Combination Sum (39) - HF  
- Combination Sum II (40)  

# 🌅 LeetCode Handbook 

## Phase 1: Fundamentals 
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

👉 If you can use key, always use key (more efficient).
👉 Only use <mark>cmp_to_key when you need a custom comparison rule.</mark>

**Sample**
- Input: `[3, 30, 34, 5, 9]`
- Output: `"3033459"`

**Idea (Greedy + Custom Sort):**
Sort numbers (as strings) by comparator on concatenations: `x+y < y+x` → `x` comes first. Edge case: all zeros → return `"0"`.

```python
from functools import cmp_to_key
from typing import List

def min_number(nums: List[int]) -> str:
    strs = list(map(str, nums))  # map(func, iterable)

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

**📌 Difference: <mark>sorted() vs list.sort()</mark>**

- list.sort(): Sorts in place, directly modifies the original list, and returns None.
- sorted(): Creates a new list, does not modify the original object, and returns the sorted list.

```python
nums = [3, 1, 4, 1, 5, 9]
print(sorted(nums))         # [1, 1, 3, 4, 5, 9]
print(sorted(nums, reverse=True))  # [9, 5, 4, 3, 1, 1]

scores = {"Tom": 90, "Alice": 85, "Bob": 95}

print(sorted(scores))  
# ['Alice', 'Bob', 'Tom']

print(sorted(scores.items(), key=lambda x: x[1]))  
# [('Alice', 85), ('Tom', 90), ('Bob', 95)]
```

#### 1.6 Search Insert Position - Binary Search lower_bound

Problem: Return the index if the target is found; otherwise, return the index where it would be inserted in order.

```
Input: nums = [1,3,5,6], target = 5 → Output: 2
Input: nums = [1,3,5,6], target = 2 → Output: 1
```

Idea (Binary Search): Standard lower_bound. - nums[m] >= target

```python
from typing import List

def search_insert(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:   # The answer is on the right.
            l = m + 1
        else:          # nums[m] >= target
            r = m
    return l

# Examples
print(search_insert([1,3,5,6], 5))  # 2
print(search_insert([1,3,5,6], 2))  # 1
```
 

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
| --- | --- | ---------- | ---------- | --- | ----- | ---- | ---- | ---- |
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

#### 1) Longest Substring Without Repeating Characters — LeetCode 3 (HF)

**Problem**  
Given a string `s`, find the length of the longest substring without repeating characters.

**Sample**  
- Input: `s = "abcabcbb"`  
- Output: `3`  (substring `"abc"`)

**Approach (Sliding Window + Hash Map)**  
Expand right; if a char repeats inside the window, move left to `last_index[char] + 1`. Track max length.

```python
def lengthOfLongestSubstring(s: str) -> int:
    last = {}         # char -> last seen index
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best

# Example
print(lengthOfLongestSubstring("abcabcbb"))  # 3
```

#### 2) Continuous Sequence Sum Equals Target — (Consecutive Positive Integers)

**Problem**  
Find all sequences of consecutive positive integers (length ≥ 2) that sum to `target`.

**Sample**  
- Input: `target = 15`  
- Output: `[[1,2,3,4,5], [4,5,6], [7,8]]`

**Approach (Two Pointers Sliding Window)**  
Use a window `[left, right]` over positive integers, maintain current sum, expand/shrink accordingly.

```python
def find_continuous_sequence(target: int):
    if target < 3:
        return []
    res = []
    left, right = 1, 2
    curr = left + right
    limit = target // 2 + 1  # shortest window has length 2

    while left < right and right <= limit:
        if curr == target:
            res.append(list(range(left, right + 1)))
            curr -= left
            left += 1
        elif curr < target:
            right += 1
            curr += right
        else:
            curr -= left
            left += 1
    return res

# Example
print(find_continuous_sequence(15))  # [[1,2,3,4,5],[4,5,6],[7,8]]
```

#### 3) Sliding Window Maximum — LeetCode 239 (HF)

**Problem**  
Given an array `nums` and an integer `k`, return a list of the max value in each window of size `k`.

**Sample**  
- Input: `nums = [1,3,-1,-3,5,3,6,7], k = 3`  
- Output: `[3,3,5,5,6,7]`

**Approach (Monotonic Deque)**  
Keep a deque of indices with values in decreasing order; pop out-of-window indices and smaller tails.

```python
from collections import deque
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    dq = deque()   # store indices, values monotone decreasing
    ans = []
    for i, x in enumerate(nums):
        # remove indices out of window
        while dq and dq[0] <= i - k:
            dq.popleft()
        # maintain decreasing values
        while dq and nums[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        # output when window is formed
        if i >= k - 1:
            ans.append(nums[dq[0]])
    return ans

# Example
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
```

#### 4) Minimum Window Substring — LeetCode 76 (HF)

**Problem**  
Given strings `s` and `t`, return the minimum window in `s` that contains all characters of `t`. If not found, return `""`.

**Sample**  
- Input: `s = "ADOBECODEBANC"`, `t = "ABC"`  
- Output: `"BANC"`

**Approach (Sliding Window + Frequency Counters)**  
Expand right to satisfy all `t` counts; then shrink left to minimize. Track best window.

```python
from collections import Counter

def minWindow(s: str, t: str) -> str:
    need = Counter(t)
    missing = len(t)       # how many chars still missing to satisfy need
    left = 0
    best_len = float('inf')
    best = (0, 0)
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1

        # When all required chars are covered, try to shrink from left
        while missing == 0:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best = (left, right + 1)
            # Move left: restore need for s[left]
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    return s[best[0]:best[1]] if best_len != float('inf') else ""

# Example
print(minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
```

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


## Phase 3: Linked List

- Merge Two Sorted Lists (21) - HF  
- Reverse Linked List (206) - HF  
- Remove Duplicates from Sorted List II (82)  
- Linked List Cycle (141) - HF  

#### 3.1 Merge Two Sorted Lists — LeetCode 21 (HF)

**Problem**  
Merge two sorted linked lists into one sorted list.

**Sample**  
- Input: l1 = [1,2,4], l2 = [1,3,4]  
- Output: [1,1,2,3,4,4]

**Approach**  
Use dummy head + two pointers. Attach smaller node each time.

**Python**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
```

#### 3.2 Reverse Linked List — LeetCode 206 (HF)

**Problem**  
Reverse a singly linked list.

**Sample**  
- Input: [1,2,3,4,5]   ：  **1 → 2 → 3 → 4 → 5 → None**
- Output: [5,4,3,2,1]  ：  **5 → 4 → 3 → 2 → 1 → None**

**Approach**  
Iterative: track `prev, cur`. At each step reverse `cur.next`.  

**Python**
```python
def reverseList(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev
```

#### 3.3 Remove Duplicates from Sorted List II — LeetCode 82

**Problem**  
Given sorted linked list, delete all nodes that appear more than once.

**Sample**  
- Input: [1,2,3,3,4,4,5]  
- Output: [1,2,5]

**Approach**  
Dummy head + two pointers. Skip nodes with duplicates.  

**Python**
```python
def deleteDuplicates(head):
    dummy = ListNode(0, head)
    prev, cur = dummy, head
    while cur:
        if cur.next and cur.val == cur.next.val:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            prev.next = cur.next
        else:
            prev = prev.next
        cur = cur.next
    return dummy.next
```


#### 3.4 Linked List Cycle — LeetCode 141 (HF)

**Problem**  
Detect if a linked list has a cycle.  

**Sample**  
- Input: head = [3,2,0,-4], tail connects to node index 1  
- Output: True  

**Approach**  
Fast and slow pointers. If they meet → cycle.  

```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast: return True
    return False
```

## Phase 4: Dynamic Programming

### Basics
- Climbing Stairs (70) - HF  
- House Robber (198) - HF  
- Longest Increasing Subsequence (300)  
- Coin Change (322) - HF  

### Grid / Paths
- Unique Paths (62) - HF  
- Unique Paths II (63)  
- Minimum Path Sum (64) - HF  

### Stocks
- Best Time to Buy and Sell Stock I (121) - HF  
- Best Time to Buy and Sell Stock II (122) - HF  
- Best Time to Buy and Sell Stock with Cooldown (309)  
- Best Time to Buy and Sell Stock with Fee (714)  
- Best Time to Buy and Sell Stock III (123)  

### Strings
- Longest Palindromic Substring (5)  
- Edit Distance (72)  
- Longest Common Subsequence (1143)  
- Word Break (139) - HF  

### 4.1 Basics

#### 1) Climbing Stairs — LeetCode 70

**Sample**  

- Input: `n = 3`  
- Output: `3`  (ways: `[1+1+1], [1+2], [2+1]`)

**Approach**  

- DP relation: `dp[i] = dp[i-1] + dp[i-2]`  
- Base: `dp[1] = 1`, `dp[2] = 2`

```python
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

#### 2) House Robber — LeetCode 198
**Problem**  
Given a row of houses with non-negative integer money, you cannot rob adjacent houses. Return the maximum amount you can rob.

**Sample**  

- Input: `nums = [2,7,9,3,1]`  
- Output: `12` (rob houses with 2, 9, 1)

**Approach**  

- DP: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`  
- Base: `dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])`

```python
from typing import List

def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]
```

#### 3) Longest Increasing Subsequence — LeetCode 300
**Problem**  
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

**Sample**  

- Input: `nums = [10,9,2,5,3,7,101,18]`  
- Output: `4` (one LIS is `[2,3,7,101]`)

**Approach**  

- O(n²) DP: `dp[i] = max(dp[i], dp[j]+1)` for all `j < i` where `nums[i] > nums[j]`  
- Initialize `dp[i] = 1`

```python
from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

#### 4) Coin Change — LeetCode 322 （Unbounded knapsack DP）

**Problem**  
Given coins of different denominations and a total amount, return the fewest number of coins to make up that amount. If not possible, return `-1`.

**Sample**  

- Input: `coins = [1,2,5], amount = 11`  
- Output: `3` (11 = 5 + 5 + 1)

**Approach**  

- Unbounded knapsack DP.  
- Initialize `dp = [0] + [inf] * amount`.  
- Transition: `dp[x] = min(dp[x], dp[x - c] + 1)` for each coin `c` and `x >= c`.

```python
from typing import List
import math

def coinChange(coins: List[int], amount: int) -> int:
    dp = [math.inf] * (amount + 1)
    dp[0] = 0
    for c in coins:
        for x in range(c, amount + 1):
            dp[x] = min(dp[x], dp[x - c] + 1)
    return dp[amount] if dp[amount] != math.inf else -1
```

### 4.2 Grid / Paths
- Unique Paths
- Unique Paths II
- Minimum Path Sum

### 4.2 Grid / Paths

#### 1) Unique Paths — LeetCode 62

**Problem**  
A robot is located at the top-left of an `m x n` grid and can only move right or down. How many unique paths to bottom-right?

**Sample**  
- Input: `m = 3, n = 7`  
- Output: `28`

**Approach**  
- DP with `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.     
- Initialize the first row/column to 1.  

```python
def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

# Example
print(uniquePaths(3, 7))  # 28
```

#### 2) Unique Paths II — LeetCode 63

**Problem**
A robot is located at the top-left of an `m x n` grid and can only move right or down. Some cells are blocked by obstacles (`1`).
Find the number of unique paths to bottom-right.

**Sample**

* Input:

  ```
  obstacleGrid =
  [
    [0,0,0],
    [0,1,0],
    [0,0,0]
  ]
  ```
* Output: `2`

**Approach**

* DP with `dp[i][j] = dp[i-1][j] + dp[i][j-1]` if no obstacle.
* If obstacle at `[i][j]`, set `dp[i][j] = 0`.

```python
from typing import List

def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    
    # Start position
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    
    # Fill dp table
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    
    return dp[-1][-1]

# Example
print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))  # 2
```


#### 3) Minimum Path Sum — LeetCode 64

**Problem**
Given a grid filled with non-negative numbers, find a path from top-left to bottom-right that minimizes the sum of all numbers along the path.
You can only move right or down.

**Sample**

* Input:

  ```
  grid =
  [
    [1,3,1],
    [1,5,1],
    [4,2,1]
  ]
  ```
* Output: `7`
  (Path = `1 → 3 → 1 → 1 → 1`)

**Approach**

* DP with `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`.
* Initialize first row and first column.

```python
from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[0][0] = grid[0][0]
    
    # First row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    # First column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    
    # Rest of grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    
    return dp[-1][-1]

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # 7
```


### 4.3 Stocks

#### 1) Best Time to Buy and Sell Stock I — LeetCode 121

**Problem**  
Given an array of prices, find the maximum profit with **one transaction** (buy once, sell once).

**Sample**  
- Input: `prices = [7,1,5,3,6,4]`  
- Output: `5` (buy at 1, sell at 6)

**Approach**  
- Track minimum price seen so far.  
- Profit = `price - min_price`.  
- Update max profit each day.  

```python
from typing import List

def maxProfit_I(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

# Example
print(maxProfit_I([7,1,5,3,6,4]))  # 5
```


#### 2) Best Time to Buy and Sell Stock II — LeetCode 122

**Problem**
You can complete multiple transactions (buy and sell many times).
Find the maximum profit.

**Sample**

* Input: `prices = [7,1,5,3,6,4]`
* Output: `7` (buy at 1→sell at 5, buy at 3→sell at 6)

**Approach - Greedy**

* Every increase contributes to profit.
* Sum all `prices[i] - prices[i-1]` where positive.

```python
def maxProfit_II(prices: List[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

# Example
print(maxProfit_II([7,1,5,3,6,4]))  # 7
```

**Approach - DP**

```python
hold, cash = -prices[0], 0
for price in prices[1:]:
    hold = max(hold, cash - price)
    cash = max(cash, hold + price)
return cash
```

#### 3) Best Time to Buy and Sell Stock with Cooldown — LeetCode 309

**Problem**
You may not buy stock the day right after selling (cooldown 1 day).

**Sample**

* Input: `prices = [1,2,3,0,2]`
* Output: `3`

**Approach (DP)**

* `hold[i]`: max profit when holding stock.
* `sold[i]`: max profit when just sold.
* `rest[i]`: max profit when cooldown.

```python
def maxProfit_cooldown(prices: List[int]) -> int:
    if not prices:
        return 0
    n = len(prices)
    hold = [-float('inf')] * n
    sold = [0] * n
    rest = [0] * n

    hold[0] = -prices[0]
    for i in range(1, n):
        hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
        sold[i] = hold[i - 1] + prices[i]
        rest[i] = max(rest[i - 1], sold[i - 1])
    return max(sold[-1], rest[-1])

# Example
print(maxProfit_cooldown([1,2,3,0,2]))  # 3
```


#### 4) Best Time to Buy and Sell Stock with Fee — LeetCode 714

**Problem**
You pay a transaction fee for each trade.

**Sample**

* Input: `prices = [1,3,2,8,4,9]`, `fee = 2`
* Output: `8`

**Approach (DP)**

* `hold`: max profit when holding stock.
* `cash`: max profit when not holding.

```python
def maxProfit_fee(prices: List[int], fee: int) -> int:
    hold, cash = -prices[0], 0
    for price in prices[1:]:
        hold = max(hold, cash - price)
        cash = max(cash, hold + price - fee)
    return cash

# Example
print(maxProfit_fee([1,3,2,8,4,9], 2))  # 8
```

---

#### 5) Best Time to Buy and Sell Stock III — LeetCode 123

**Problem**
At most 2 transactions.

**Sample**

* Input: `prices = [3,3,5,0,0,3,1,4]`
* Output: `6`

**Approach (DP)**

* Track 4 states: buy1, sell1, buy2, sell2.

```python
def maxProfit_III(prices: List[int]) -> int:
    buy1, sell1 = float('-inf'), 0
    buy2, sell2 = float('-inf'), 0
    for p in prices:
        buy1 = max(buy1, -p)
        sell1 = max(sell1, buy1 + p)
        buy2 = max(buy2, sell1 - p)
        sell2 = max(sell2, buy2 + p)
    return sell2

# Example
print(maxProfit_III([3,3,5,0,0,3,1,4]))  # 6
```

### 4.4 Strings

#### 1) Longest Palindromic Substring — LeetCode 5

**Problem**
Find the longest palindromic substring in a given string.

**Sample**

* Input: `s = "babad"`
* Output: `"bab"` (or `"aba"`)

**Approach (DP)**

* `dp[i][j] = True` if `s[i] == s[j]` and inside substring is palindrome.

```python
def longestPalindrome(s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    ans = ""
    for l in range(n):
        for i in range(n - l):
            j = i + l
            if s[i] == s[j] and (l < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if l + 1 > len(ans):
                    ans = s[i:j+1]
    return ans

# Example
print(longestPalindrome("babad"))  # "bab" or "aba"
```

#### 2) Edit Distance — LeetCode 72

**Problem**
Given two words, find the minimum operations (insert, delete, replace) to convert word1 to word2.

**Sample**

* Input: `word1 = "horse"`, `word2 = "ros"`
* Output: `3`

**Approach (DP)**

* `dp[i][j]`: min ops to convert `word1[:i]` to `word2[:j]`.

```python
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

# Example
print(minDistance("horse", "ros"))  # 3
```


#### 3) Longest Common Subsequence — LeetCode 1143

**Problem**
Find the length of longest subsequence common to two strings.

**Sample**

* Input: `text1 = "abcde"`, `text2 = "ace"`
* Output: `3`

**Approach (DP)**

* `dp[i][j]`: LCS of `text1[:i]`, `text2[:j]`.

```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# Example
print(longestCommonSubsequence("abcde", "ace"))  # 3
```

#### 4) Word Break — LeetCode 139

**Problem**
Given a string and a dictionary of words, determine if the string can be segmented into dictionary words.

**Sample**

* Input: `s = "leetcode"`, `wordDict = ["leet","code"]`
* Output: `True`

**Approach (DP)**

* `dp[i]`: can `s[:i]` be segmented.

```python
from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    wordSet = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[n]

# Example
print(wordBreak("leetcode", ["leet","code"]))  # True
```

## Phase 5: DFS / BFS

- Word Search in Matrix (LeetCode 79) → HF
- Robot Movement Range (Offer 13) → HF
- Number of Islands (200) → HF
- Course Schedule (207) → HF
- Course Schedule II (210) → HF

#### 5.1 Word Search in Matrix — LeetCode 79

**Problem**  
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from sequentially adjacent cells (horizontally or vertically), but the same letter cell cannot be used more than once.

**Sample**  
- Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"  
- Output: True  

**Approach**  
- Use DFS with backtracking.  
- Mark visited cell temporarily, explore 4 directions, then restore.  

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
            return False
        tmp, board[i][j] = board[i][j], "#"
        found = (dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1))
        board[i][j] = tmp
        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True
    return False
```

#### 5.2 Robot Movement Range (BFS) — Offer 13

**Problem**
A robot starts at (0,0) in an m×n grid. It can move up/down/left/right, but cannot enter a cell where the sum of digits of row+col > k. Count how many cells can be reached.

**Sample**

* Input: m=2, n=3, k=1
* Output: 3

**Approach**

* BFS from (0,0).
* Check digit sum constraint, use visited set.

```python
def movingCount(m: int, n: int, k: int) -> int:
    from collections import deque
    def digit_sum(x): return sum(map(int, str(x)))
    q = deque([(0,0)])
    visited = set()
    while q:
        i,j = q.popleft()
        if not (0 <= i < m and 0 <= j < n): continue
        if digit_sum(i)+digit_sum(j) > k or (i,j) in visited: continue
        visited.add((i,j))
        q.append((i+1,j)); q.append((i,j+1))
    return len(visited)
```


#### 5.3 Number of Islands — LeetCode 200

**Problem**
Given a 2D grid of '1' (land) and '0' (water), count the number of islands.

**Sample**

* Input: grid =

```
11110
11010
11000
00000
```

* Output: 1

**Approach**

* DFS flood fill. Mark visited as '0'.


```python
def numIslands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    def dfs(i,j):
        if i<0 or j<0 or i>=rows or j>=cols or grid[i][j] != "1": return
        grid[i][j] = "0"
        dfs(i+1,j); dfs(i-1,j); dfs(i,j+1); dfs(i,j-1)

    count=0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]=="1":
                dfs(i,j); count+=1
    return count
```


#### 5.4 Course Schedule — LeetCode 207

**Problem**
Given numCourses and prerequisites, check if you can finish all courses (detect cycle in directed graph).

**Sample**

* Input: numCourses=2, prerequisites=\[\[1,0]]
* Output: True

**Approach**

* Use topological sort (BFS indegree).
* If processed count == numCourses → True.

```python
from collections import deque

def canFinish(numCourses, prerequisites):
    indeg = [0]*numCourses
    g = [[] for _ in range(numCourses)]
    for a,b in prerequisites:
        g[b].append(a)
        indeg[a]+=1
    q = deque([i for i in range(numCourses) if indeg[i]==0])
    visited=0
    while q:
        u=q.popleft(); visited+=1
        for v in g[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    return visited==numCourses
```


#### 5.5 Course Schedule II — LeetCode 210

**Problem**
Return one valid order to finish all courses (topological ordering).

**Sample**

* Input: numCourses=2, prerequisites=\[\[1,0]]
* Output: \[0,1]

**Approach**

* BFS topological sort, collect order.

```python
def findOrder(numCourses, prerequisites):
    from collections import deque
    indeg = [0]*numCourses
    g=[[] for _ in range(numCourses)]
    for a,b in prerequisites:
        g[b].append(a); indeg[a]+=1
    q=deque([i for i in range(numCourses) if indeg[i]==0])
    order=[]
    while q:
        u=q.popleft(); order.append(u)
        for v in g[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    return order if len(order)==numCourses else []
```


## Phase 6: Greedy

- Jump Game I (55) - HF
- Jump Game II (45) - HF
- Gas Station (134) - HF


## Phase 6: Greedy

#### 6.1 Jump Game I — LeetCode 55

**Problem**  
Given an array `nums` where each element represents your maximum jump length at that position, determine if you can reach the last index.

**Sample**  
- Input: `nums = [2,3,1,1,4]`  
  Output: `True`   # can jump 0→1→4  
- Input: `nums = [3,2,1,0,4]`  
  Output: `False`  # stuck at index 3  

**Approach**  
- Track the farthest index you can reach.  
- If at any point `i > farthest`, you cannot proceed → return False.  
- Otherwise, update `farthest = max(farthest, i + nums[i])`.  

```python
from typing import List

def canJump(nums: List[int]) -> bool:
    farthest = 0
    for i, step in enumerate(nums):
        if i > farthest:   # cannot reach this position
            return False
        farthest = max(farthest, i + step)
    return True

# Quick checks
print(canJump([2,3,1,1,4]))  # True
print(canJump([3,2,1,0,4]))  # False
```

#### 6.2 Jump Game II — LeetCode 45

**Problem**  
Given an array `nums` where each element represents your maximum jump length, return the minimum number of jumps to reach the last index.

**Sample**  
- Input: `nums = [2,3,1,1,4]`  
  Output: `2`   # jump 0→1→4  
- Input: `nums = [1,2,1,1,1]`  
  Output: `3`   # jump 0→1→2→4  

**Approach**  
- Greedy: Track `current_end` (farthest we can reach in current jump) and `farthest` (max reach so far).  
- When index `i == current_end`, we need one more jump and update `current_end = farthest`.  

```python
from typing import List

def jump(nums: List[int]) -> int:
    jumps = 0
    farthest = 0
    current_end = 0
    for i in range(len(nums) - 1):  # no need to jump from last index
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps

# Quick checks
print(jump([2,3,1,1,4]))  # 2
print(jump([1,2,1,1,1]))  # 3
```

#### 6.3 Gas Station — LeetCode 134

**Problem**  
There are `n` gas stations along a circular route, where `gas[i]` is the gas at station `i`, and `cost[i]` is the cost to travel from `i` to `i+1`.  
Return the starting gas station’s index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`.

**Sample**  
- Input:  
  `gas  = [1,2,3,4,5]`  
  `cost = [3,4,5,1,2]`  
  Output: `3`   # start at station 3  
- Input:  
  `gas  = [2,3,4]`  
  `cost = [3,4,3]`  
  Output: `-1`  # impossible  

**Approach**  
- If `total gas < total cost`, impossible → return -1.  
- Otherwise, greedy: if `tank < 0` at station `i`, reset `start = i+1` and `tank = 0`.  

```python
from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    total, tank, start = 0, 0, 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:   # cannot continue, reset starting point
            start = i + 1
            tank = 0
    return start if total >= 0 else -1

# Quick checks
print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # 3
print(canCompleteCircuit([2,3,4], [3,4,3]))          # -1
```

## Phase 7: Backtracking

- Subsets (78) — HF
- Subsets II (90) — HF
- Permutations (46) — HF
- Permutations II (47) — HF
- Combination Sum (39) — HF
- Combination Sum II (40) — HF

#### 7.1 Subsets — LeetCode 78

**Problem**  
Return all possible subsets (the power set) of an array of distinct integers.

**Sample**  
- Input: `nums = [1,2,3]`  
- Output: `[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]`

**Approach**  
Backtrack over indices; at each index choose “take” or “not take”.

```python
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    res, path = [], []
    def dfs(i: int):
        if i == len(nums):
            res.append(path[:]); return
        # not take
        dfs(i + 1)
        # take
        path.append(nums[i])
        dfs(i + 1)
        path.pop()
    dfs(0)
    return res
```

#### 7.2 Subsets II — LeetCode 90

**Problem**
Return all subsets where `nums` may contain duplicates (results must be unique).

**Sample**

* Input: `nums = [1,2,2]`
* Output: `[[],[1],[2],[1,2],[2,2],[1,2,2]]`

**Approach**
Sort first; during a level, skip same values: if `i > start and nums[i]==nums[i-1]` → continue.


```python
from typing import List

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res, path = [], []
    def dfs(start: int):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    dfs(0)
    return res

# Quick check
print(subsetsWithDup([1,2,2]))
```

#### 7.3 Permutations — LeetCode 46

**Problem**
Return all permutations of distinct integers.

**Sample**

* Input: `nums = [1,2,3]`
* Output: `[[1,2,3],[1,3,2],[2,1,3],...]`

**Approach**
Backtrack with a `used` array or swap in-place.


```python
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    res, path = [], []
    used = [False] * len(nums)

    def dfs():
        if len(path) == len(nums):
            res.append(path[:]); return
        for i, v in enumerate(nums):
            if used[i]: 
                continue
            used[i] = True
            path.append(v)
            dfs()
            path.pop()
            used[i] = False
    dfs()
    return res

# Quick check
print(permute([1,2,3]))
```

#### 7.4 Permutations II — LeetCode 47

**Problem**
Return all unique permutations when `nums` can contain duplicates.

**Sample**

* Input: `nums = [1,1,2]`
* Output: `[[1,1,2],[1,2,1],[2,1,1]]`

**Approach**
Sort; skip duplicates within the same depth:
`if i>0 and nums[i]==nums[i-1] and not used[i-1]: continue`.


```python
from typing import List

def permuteUnique(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res, path = [], []
    used = [False] * len(nums)

    def dfs():
        if len(path) == len(nums):
            res.append(path[:]); return
        for i in range(len(nums)):
            if used[i]: 
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                # avoid generating duplicates at this depth
                continue
            used[i] = True
            path.append(nums[i])
            dfs()
            path.pop()
            used[i] = False
    dfs()
    return res

# Quick check
print(permuteUnique([1,1,2]))
```

#### 7.5 Combination Sum — LeetCode 39

**Problem**
Given distinct candidates and a target, find all unique combinations where the chosen numbers sum to target (a number may be used unlimited times).

**Sample**

* Input: `candidates = [2,3,6,7], target = 7`
* Output: `[[7],[2,2,3]]`

**Approach**
Backtrack with index `start`; allow reuse by passing same `i` in next call. Prune when sum exceeds target.


```python
from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res, path = [], []

    def dfs(start: int, remain: int):
        if remain == 0:
            res.append(path[:]); return
        for i in range(start, len(candidates)):
            v = candidates[i]
            if v > remain:
                break
            path.append(v)
            dfs(i, remain - v)  # reuse allowed
            path.pop()
    dfs(0, target)
    return res

# Quick check
print(combinationSum([2,3,6,7], 7))
```


#### 7.6 Combination Sum II — LeetCode 40

**Problem**
Given candidates (may contain duplicates) and a target, each number can be used once. Return unique combinations.

**Sample**

* Input: `candidates = [10,1,2,7,6,1,5], target = 8`
* Output: `[[1,1,6],[1,2,5],[1,7],[2,6]]`

**Approach**
Sort, skip duplicates at the same `start` level, and advance index (`i+1`) to avoid reusing same element.


```python
from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res, path = [], []

    def dfs(start: int, remain: int):
        if remain == 0:
            res.append(path[:]); return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue  # skip same value at this depth
            v = candidates[i]
            if v > remain:
                break
            path.append(v)
            dfs(i + 1, remain - v)  # each element used once
            path.pop()
    dfs(0, target)
    return res

# Quick check
print(combinationSum2([10,1,2,7,6,1,5], 8))
```

