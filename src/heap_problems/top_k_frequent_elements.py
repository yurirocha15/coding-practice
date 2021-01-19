#!/usr/bin/env python
"""
Platform: LeetCode
347. Top K Frequent Elements
URL: https://leetcode.com/problems/top-k-frequent-elements/

Description:
Given a non-empty array of integers, return the k most frequent elements.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [n for n, _ in Counter(nums).most_common(k)]


if __name__ == "__main__":
    solution = Solution()
    assert solution.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert solution.topKFrequent([1], 1) == [1]
