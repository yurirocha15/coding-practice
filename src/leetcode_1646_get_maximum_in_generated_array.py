# @l2g 1646 python3
# [1646] Get Maximum in Generated Array
# Difficulty: Easy
# https://leetcode.com/problems/get-maximum-in-generated-array
#
# You are given an integer n. An array nums of length n + 1 is generated in the following way:
#
# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
#
# Return the maximum integer in the array nums​​​.
#
# Example 1:
#
# Input: n = 7
# Output: 3
# Explanation: According to the given rules:
#   nums[0] = 0
#   nums[1] = 1
#   nums[(1 * 2) = 2] = nums[1] = 1
#   nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
#   nums[(2 * 2) = 4] = nums[2] = 1
#   nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
#   nums[(3 * 2) = 6] = nums[3] = 2
#   nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
# Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.
#
# Example 2:
#
# Input: n = 2
# Output: 1
# Explanation: According to the given rules, the maximum between nums[0], nums[1], and nums[2] is 1.
#
# Example 3:
#
# Input: n = 3
# Output: 2
# Explanation: According to the given rules,the maximum between nums[0],nums[1],nums[2],
# and nums[3] is 2.
#
#
# Constraints:
#
# 0 <= n <= 100
#
#

"""
You are given an integer n. An array nums of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums​​​.

Example 1:

Input: n = 7
Output: 3
Explanation: According to the given rules:
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.
Example 2:

Input: n = 2
Output: 1
Explanation: According to the given rules, the maximum between nums[0], nums[1], and nums[2] is 1.
Example 3:

Input: n = 3
Output: 2
Explanation: According to the given rules, the maximum between nums[0], nums[1], nums[2], and nums[3] is 2.
 

Constraints:

0 <= n <= 100

"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # corner cases
        if n <= 1:
            return n

        # we dont need to store the whole array to find the maximum value
        # the array maximum needed size is n/2 + 2
        max_len = int(n / 2) + 2
        # initialize the array
        tmp = [0] * max_len
        tmp[1] = 1
        ret = 0
        for i in range(1, max_len):
            max_tmp = tmp[i]
            # only store the values that we will need in the future
            if 2 * i < max_len:
                tmp[2 * i] = tmp[i]
            if 2 * i + 1 < max_len:
                tmp[2 * i + 1] = tmp[i] + tmp[i + 1]
            # check if one of the newly calculated values are the current max
            if 2 * i + 1 <= n:
                max_tmp = max(max_tmp, tmp[i] + tmp[i + 1])
            ret = max(ret, max_tmp)
        return ret


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1646.py")])
