# 🌅 LeetCode Handbook 

## 1: Fundamentals

### Arrays & Hashing

- Two Sum (HashMap)
- Maximum Subarray
- Product of Array Except Self


**1. Two Sum (HashMap)**

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


**2. Maximum Subarray - DP**

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


**3. Product of Array Except Self**

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


#### Arrays & Sorting
- Sort Array (Quick Sort, Merge Sort)
- Merge Sorted Array (two pointers, reverse order)
- Arrange Array to Minimum Number (cmp_to_key)
- Search Insert Position
- Spiral Matrix Printing
- Merge Intervals
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
