#!/usr/bin/env python
"""
Platform: LeetCode
1695. Maximum Erasure Value
URL: https://leetcode.com/problems/maximum-erasure-value/

Description:
You are given an array of positive integers nums
and want to erase a subarray containing unique elements.
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms
a contiguous subsequence of a, that is,
if it is equal to a[l],a[l+1],...,a[r] for some (l,r).


Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
"""
from typing import List, Set


class Solution:
    def maximum_unique_subarray(self, nums: List[int]) -> int:
        # cur_sum stores the current sum
        left = right = ret = cur_sum = 0
        # the stash stores the values between the two pointers
        stash: Set[int] = set()
        # loop until the right pointer arrives to the end of the list
        while right < len(nums):
            # if the current number is already in the stash, we should move the left pointer until it isn't
            while nums[right] in stash:
                # remove the left value from the current sum
                cur_sum -= nums[left]
                # also remove from the stash
                stash.remove(nums[left])
                # move the left pointer
                left += 1
            # add the current number to the stash
            stash.add(nums[right])
            # also add to the current sum
            cur_sum += nums[right]
            # move the right pointer
            right += 1
            # check if the current sum is bigger than the current return value
            ret = max(ret, cur_sum)
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximum_unique_subarray([4, 2, 4, 5, 6]) == 17
    assert solution.maximum_unique_subarray([5, 2, 1, 2, 5, 2, 1, 2, 5]) == 8
