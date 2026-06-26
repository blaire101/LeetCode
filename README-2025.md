

### 2. d**ynamic programming**

1. **Climbing Stairs**  LeetCode 70 ( for i in range(3, n + 1): dp[i] = dp[i - 1] + dp[i - 2] ) ✅
2. **House Robber** - LeetCode 198 ( dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]) )✅
3. Longest Increasing Subsequence ( **dual circulation -** if nums[i] > nums[j]:)✅
4. **Coin Change** - LeetCode 322 （dp = [float('inf')] * (amount + 1)） dp[x] = min(dp[x], dp[x - coin] + 1) ✅
5. **Longest Palindromic Substring (回文)** - LeetCode 5 难
6. **Edit Distance** - LeetCode 72 ✅
7. **Unique Paths** - LeetCode 62 ✅
8. **Best Time to Buy and Sell Stock I one buy and one sell** - LeetCode 121 （max_profit = max(max_profit, price - min_price)）
9. **Best Time to Buy and Sell Stock II** - LeetCode 122 -  max_profit += prices[i] - prices[i - 1]
10. **Best Time to Buy and Sell Stock with Cooldown** - LeetCode 309 难


#### 1) Climbing Stairs — LeetCode 70

**Sample**  

- Input: `n = 3`  
- Output: `3`  (ways: `[1+1+1], [1+2], [2+1]`)

**Approach**  

- DP relation: `dp[i] = dp[i-1] + dp[i-2]`  
- Base: `dp[1] = 1`, `dp[2] = 2`

**Python**

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

**Python**

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

**Python**

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

#### 4) Coin Change — LeetCode 322

**Problem**  
Given coins of different denominations and a total amount, return the fewest number of coins to make up that amount. If not possible, return `-1`.

**Sample**  

- Input: `coins = [1,2,5], amount = 11`  
- Output: `3` (11 = 5 + 5 + 1)

**Approach**  

- Unbounded knapsack DP.  
- Initialize `dp = [0] + [inf] * amount`.  
- Transition: `dp[x] = min(dp[x], dp[x - c] + 1)` for each coin `c` and `x >= c`.

**Python**

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

#### 5) Longest Palindromic Substring — LeetCode 5

**Problem**  
Given a string `s`, return the longest palindromic substring in `s`.

**Sample**  

- Input: `s = "babad"`  
- Output: `"bab"` or `"aba"`

**Approach**  

- DP: `dp[i][j] = True` if `s[i] == s[j]` and `(j - i < 3 or dp[i+1][j-1])`.  
- Track longest range.

**Python**

```python
def longestPalindrome(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1
    for j in range(n):
        for i in range(j + 1):
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i + 1 > max_len:
                    start, max_len = i, j - i + 1
    return s[start:start + max_len]
```

## 6) Edit Distance — LeetCode 72
**Problem**  
Return the minimum number of operations (insert, delete, replace) to convert `word1` into `word2`.

**Sample**  

- Input: `word1 = "horse", word2 = "ros"`  
- Output: `3`

**Approach**  

- Let `dp[i][j]` be the edit distance between `word1[:i]` and `word2[:j]`.  
- If last chars equal: `dp[i][j] = dp[i-1][j-1]`; else `1 + min(delete, insert, replace)`.

**Python**

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
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # delete
                    dp[i][j - 1],    # insert
                    dp[i - 1][j - 1] # replace
                )
    return dp[m][n]
```

#### 7) Unique Paths — LeetCode 62

**Problem**  
A robot is located at the top-left of an `m x n` grid and can only move right or down. How many unique paths to bottom-right?

**Sample**  

- Input: `m = 3, n = 7`  
- Output: `28`

**Approach**  

- DP with `dp[i][j] = dp[i-1][j] + dp[i][j-1]`, initialize first row/column to 1.

**Python**

```python
def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
```

#### 8) Best Time to Buy and Sell Stock I — LeetCode 121
**Problem**  
One transaction allowed: buy once and sell once. Maximize profit.

**Sample**  

- Input: `prices = [7,1,5,3,6,4]`  
- Output: `5` (buy at 1, sell at 6)

**Approach**  

- Track `min_price` so far and `max_profit = max(max_profit, price - min_price)`.

**Python**

```python
from typing import List

def maxProfit_121(prices: List[int]) -> int:
    min_price, max_profit = float('inf'), 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit
```

#### 9) Best Time to Buy and Sell Stock II — LeetCode 122
**Problem**  
Unlimited transactions (but must sell before buying again). Maximize profit.

**Sample**  

- Input: `prices = [7,1,5,3,6,4]`  
- Output: `7` (profits: (5-1) + (6-3))

**Approach**  

- Greedy: sum all positive price differences.

**Python**

```python
from typing import List

def maxProfit_122(prices: List[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
```

#### 10) Best Time to Buy and Sell Stock with Cooldown — LeetCode 309
**Problem**  
Unlimited transactions, but after you sell, you must cooldown one day before buying again.

**Sample**  

- Input: `prices = [1,2,3,0,2]`  
- Output: `3`

**Approach**  

- State DP with three states:  
  - `hold`: holding stock  
  - `sold`: just sold today  
  - `rest`: not holding and not in cooldown  
- Transitions:  
  - `new_hold = max(hold, rest - price)`  
  - `new_sold = hold + price`  
  - `new_rest = max(rest, sold)`  
- Initialize: `hold = -prices[0]`, `sold = 0`, `rest = 0`  
- Answer: `max(sold, rest)`

**Python**

```python
from typing import List

def maxProfit_309(prices: List[int]) -> int:
    if not prices:
        return 0
    hold, sold, rest = -prices[0], 0, 0
    for price in prices[1:]:
        new_hold = max(hold, rest - price)
        new_sold = hold + price
        new_rest = max(rest, sold)
        hold, sold, rest = new_hold, new_sold, new_rest
    return max(sold, rest)
```



---
***Approach***: Solve using dynamic programming, maintaining three states:

- `hold[i]`: The maximum profit on day `i` when holding a stock.
- `sold[i]`: The maximum profit on day `i` when not holding a stock and having just sold it.
- `rest[i]`: The maximum profit on day `i` when not holding a stock and being in the cooldown

state transition equation：

- `hold[i] = max(hold[i-1], rest[i-1] - prices[i])`
- `sold[i] = hold[i-1] + prices[i]`
- `rest[i] = max(rest[i-1], sold[i-1])`

```python
def maxProfit(prices):
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

```

1. **Best Time to Buy and Sell Stock with Transaction Fee** - LeetCode 714

Example Data: Let’s consider an example where:

- `prices = [1, 3, 2, 8, 4, 9]`
- `fee = 2`

To solve this, we use dynamic programming and maintain two states:

- `hold`: The maximum profit when holding a stock on day `i`.
- `cash`: The maximum profit when not holding a stock on day `i`.

```python
def maxProfit(prices, fee):
    hold = -prices[0]
    cash = 0
    for price i≈n prices[1:]:
        hold = max(hold, cash - price)
        cash = max(cash, hold + price - fee)
    return cash
```

1. **Best Time to Buy and Sell Stock III** - LeetCode 123 - 最多可以完成两笔交易

### 3. leetcode linked list

1. merge 2 sorted list, Recursion
2. Reverse Linked List (while cur: cur = head.next)

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
```

---

### Phase 1: Fundamentals

---

- **Arrays and Strings**
    - Focus topics: Binary Search, Sliding Window, Prefix Sum
    - 重点题型：二分查找、滑动窗口、前缀和
    
    **1.1** Binary Search**, while l <= r ✅**
    
    ```sql
    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            if not nums:
                return -1
    
            l, r = 0, len(nums) - 1
    
            while l <= r:
                mid = (r - l)//2 + l
    
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            
            return -1
    ```
    
    https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/**✅**
    
    ```sql
    class Solution: **✅**
        def searchRange(self, nums: List[int], target: int) -> List[int]:
    
            if not nums:
                return [-1, -1]
    
            def binSearch(nums, t, flag):
                l, r = 0, len(nums) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if nums[mid] > t:
                        r = mid - 1
                    elif nums[mid] < t:
                        l = mid + 1
                    else:
                        if flag == "L":
                            r = mid - 1
                        else:
                            l = mid + 1
    
                if flag == 'L' and r + 1 < len(nums) and nums[r + 1] == t:
                    return r + 1
                if flag == 'R' and l - 1 >= 0 and nums[l - 1] == t:
                    return l - 1
                return -1
    
            return [binSearch(nums=nums, t=target, flag='L'), binSearch(nums=nums, t=target, flag='R')]
    ```
    
    [88.](https://leetcode-cn.com/problems/merge-sorted-array/) Merging two sorted arrays  - 逆向双指针 **✅**
    
    ```sql
    from typing import List **✅**
    
    class Solution:
        def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
            """
            Do not return anything, modify A in-place instead.
            """
            pa, pb, tail = m - 1, n - 1, m + n - 1
            
            while pb >= 0:
                if pa >= 0 and A[pa] > B[pb]:
                    A[tail] = A[pa]
                    pa -= 1
                else:
                    -- 因为当 pb 没有完全插入时，pa 可能已经小于0，
                    -- 这种情况下直接把 B 剩下的元素复制到 A 即可
                    A[tail] = B[pb]
                    pb -= 1
                tail -= 1
    ```
    
    https://leetcode-cn.com/problems/kth-largest-element-in-an-array/**✅**
    
    Kth Largest Element in an Array
    
    ```sql
    from heapq import heapify, heappush, heappop 
    # python中的heap是小根堆:  heapify(hp) , heappop(hp), heappush(hp, v) 
    from typing import List
    
    h
            if k == 0 or k > len(nums):
                return []
    
            hp = nums[:k]
            heapify(hp)
    
            for num in nums[k:]:
                if num > hp[0]:
                    heappop(hp)
                    heappush(hp, num)
    
            return hp[0]
    
    ```
    
    - LeetCode problems: 53, 121, 167, 209, 238
    
    要找到数组中最小的 `k` 个数，我们可以使用大顶堆（Max-Heap）来实现。通过维护一个大小为 `k` 的大顶堆，可以有效地筛选出最小的 `k` 个数。
    
    ```sql
    import heapq
    from typing import List
    
    def smallest_k_numbers(arr: List[int], k: int) -> List[int]:
        if k == 0 or not arr:
            return []
    
        # 用负数构建最大堆，取前 k 个元素
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
    
        # 遍历剩余元素，如果当前元素小于堆顶元素，则替换堆顶
        for num in arr[k:]:
            if -num > hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, -num)
    
        # 将堆中的元素还原为正数并返回
        return [-x for x in hp]
    
    # 示例
    arr = [4, 5, 1, 6, 2, 7, 3, 8]
    k = 4
    output = smallest_k_numbers(arr, k)
    print(output)  # 输出: [1, 2, 3, 4] 或其他任意顺序的 4 个最小值
    ```
    
    拼接后，最小的数字
    
    ```sql
    from functools import cmp_to_key
    
    def min_number(nums):
        def sort_rule(x, y):
            # 自定义排序规则
            if x + y < y + x:  # -1 is right， x before y after
                return -1
            elif x + y > y + x:
                return 1
            else:
                return 0
    
        strs = list(map(str, nums))
        strs.sort(key=cmp_to_key(sort_rule))
        return ''.join(strs)
    
    # 示例
    nums = [3, 30, 34, 5, 9]
    output = min_number(nums)
    print(output)  # 输出: "3033459"
    ```
    
- **Linked Lists - 递归**
    - Focus topics: Single Linked List, Double Linked List, Two Pointers
    - **Key problem types**: singly linked list, doubly linked list, fast and slow pointers
    
    merge 2 sorted linkedlist
    
    ```sql
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution:
        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            
            if l1.val < l2.val:
                p = ListNode(l1.val)
                p.next = self.mergeTwoLists(l1.next, l2)
            else:
                p = ListNode(l2.val)
                p.next = self.mergeTwoLists(l1, l2.next)
            
            return p
            
    ```
    
    - LeetCode problems: 21, 141, 142, 206, 234
    
    ```sql
    # 输入: 1->2->3->4->5->NULL
    # 输出: 5->4->3->2->1->NULL
    
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    
    class Solution(object):
        def reverseList(self, head) -> ListNode:
            if not head or not head.next:
                return head
            
            pre, cur = head, head.next
            pre.next = None
    
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
    
            return pre
    ```
    
    ```sql
    # 创建一个环：将链表的尾节点指向头节点，形成一个环。
    # 找到断开点：从头节点开始，走 𝑛 − 𝑘 % 𝑛 步，然后在这个点断开环。
    # 形成新的链表：新的链表从断开点开始，前半部分接在断开点后面
    
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    class Solution:
        def rotateRight(self, head: ListNode, k: int) -> ListNode:
            if not head or not head.next or k == 0:
                return head
            
            # 计算链表长度，并找到尾节点
            length = 1
            tail = head
            while tail.next:
                tail = tail.next
                length += 1
            
            # 将尾节点连接到头节点，形成环
            tail.next = head
            
            # 找到新的尾节点位置 (length - k % length - 1)
            new_tail_pos = length - k % length - 1
            new_tail = head
            for _ in range(new_tail_pos):
                new_tail = new_tail.next
            
            # 新的头节点是新的尾节点的下一个节点
            new_head = new_tail.next
            
            # 断开环
            new_tail.next = None
            
            return new_head
    
    # 示例用法
    # 创建链表 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    
    # 创建 Solution 对象并调用 rotateRight 方法
    solution = Solution()
    k = 3
    new_head = solution.rotateRight(head, k)
    
    # 打印结果
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else " -> NULL")
        current = current.next
    ```
    
- **Stacks and Queues**
    - Focus topics: Monotonic Stack, Priority Queue
    - 重点题型：单调栈、优先队列
    - LeetCode problems: 20, 155, 232, 739
        
        [2.1 字符串解码 “3[a2[c]]” == “accacc”](https://leetcode-cn.com/problems/decode-string/), `stack == [(3, ""), (2,"a")]`
        
        ![image.png](2%20Leetcode%2011d94e330a4580ff8c15d50cfbaf4889/image.png)
        
        ```sql
        class Solution:
            def decodeString(self, s: str) -> str:
                stack, res, multi = [], "", 0
                for c in s:
                    if c == '[':
                        stack.append([multi, res])
                        res, multi = "", 0
                    elif c == ']':
                        cur_multi, last_res = stack.pop()
                        res = last_res + cur_multi * res
                    elif '0' <= c <= '9':
                        multi = multi * 10 + int(c)            
                    else:
                        res += c
                return res
        ```
        
- Slide Window
    
    ```sql
    def find_continuous_sequence(target):
        left, right = 1, 2  # 初始化滑动窗口的左右边界
        result = []
        current_sum = left + right  # 当前窗口内数字的和
    
        while left < right:
            if current_sum == target:
                result.append(list(range(left, right + 1)))  # 如果和为target，记录序列
                current_sum -= left
                left += 1  # 将左边界右移一位
    
            elif current_sum < target:
                right += 1  # 右边界右移一位，扩大窗口
                current_sum += right
    
            else:
                current_sum -= left  # 左边界右移，缩小窗口
                left += 1
    
        return result
    
    # 示例
    target = 9
    output = find_continuous_sequence(target)
    print(output)  # 输出: [[2,3,4],[4,5]]
    
    ```
    
    ```sql
    # 65. 最长不含重复字符的子字符串 滑动窗口
    
    def length_of_longest_substring(s):
        char_map = {}  # 用于存储字符及其对应的索引
        left = 0  # 初始化滑动窗口的左边界
        max_length = 0  # 记录最长子字符串的长度
    
        for right in range(len(s)):
            # 如果字符已经在滑动窗口中，更新左边界到重复字符的下一位置
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
    
            # 更新字符在字典中的位置
            char_map[s[right]] = right
    
            # 计算当前子字符串的长度，并更新最大长度
            max_length = max(max_length, right - left + 1)
    
        return max_length
    
    # 示例
    s = "abcabcbb"
    output = length_of_longest_substring(s)
    print(output)  # 输出: 3 ("abc" 是最长的无重复字符子串)
    
    ```
    


   
    
