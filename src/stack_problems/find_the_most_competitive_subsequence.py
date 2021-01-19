#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1673. Find the Most Competitive Subsequence
URL: https://leetcode.com/problems/find-the-most-competitive-subsequence/

Description:
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length)
if in the first position where a and b differ,
subsequence a has a number less than the corresponding number in b.
For example, [1,3,4] is more competitive than [1,3,5]
because the first position they differ is at the final number, and 4 is less than 5.

Example 1:
Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence:
 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.

Example 2:
Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
1 <= k <= nums.length
"""
from typing import List


class Solution:
    def most_competitive(self, nums: List[int], k: int) -> List[int]:
        ret = nums[:k]
        n = len(nums)
        # j will keep track of the latest inclusion to the list
        j = 1
        for i, num in enumerate(nums[1:], 1):
            # go back on the ret array until:
            #  * arriving to the beggining
            #  * the preceding number is smaller
            #  * the remaining values in num would not be sufficient
            while j > 0 and num < ret[j - 1] and ((n - i) >= (k - j + 1)):
                j -= 1
            # if we are not at the end of the array, add the number and increase j
            if j < k:
                ret[j] = num
                j += 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.most_competitive([3, 5, 2, 6], 2) == [2, 6]
    assert solution.most_competitive([2, 4, 3, 3, 5, 4, 9, 6], 4) == [2, 3, 3, 4]
