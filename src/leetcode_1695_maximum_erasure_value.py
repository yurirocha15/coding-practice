# @l2g 1695 python3
# [1695] Maximum Erasure Value
# Difficulty: Medium
# https://leetcode.com/problems/maximum-erasure-value
#
# You are given an array of positive integers nums and want to erase a subarray containing unique elements.
# The score you get by erasing the subarray is equal to the sum of its elements.
# Return the maximum score you can get by erasing exactly one subarray.
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a,that is,
# if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
#
# Example 1:
#
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
#
# Example 2:
#
# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
#
#

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = r = ret = cur_sum = 0
        stash = set()
        while r < len(nums):
            while nums[r] in stash:
                cur_sum -= nums[l]
                stash.remove(nums[l])
                l += 1
            stash.add(nums[r])
            cur_sum += nums[r]
            r += 1
            ret = max(ret, cur_sum)
        return ret


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1695.py")])
