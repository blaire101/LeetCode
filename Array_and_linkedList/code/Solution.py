from typing import List
class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            hashmap[num] = i
        return None

nums = [2, 7, 10, 15]
target = 9
print(Solution.twoSum(nums, target))
# Output: [0, 1]   (2 + 7 = 9)