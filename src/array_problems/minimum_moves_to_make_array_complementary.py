#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1674. Minimum Moves to Make Array Complementary
URL: https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

Description:
You are given an integer array nums of even length n and an integer limit.
In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.

The array nums is complementary if for all indices i (0-indexed),
nums[i] + nums[n - 1 - i] equals the same number.
For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

Return the minimum number of moves required to make nums complementary.

Example 1:
Input: nums = [1,2,4,3], limit = 4
Output: 1
Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.

Example 2:
Input: nums = [1,2,2,1], limit = 2
Output: 2
Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.

Example 3:
Input: nums = [1,2,1,2], limit = 2
Output: 0
Explanation: nums is already complementary.

Constraints:

n == nums.length
2 <= n <= 10^5
1 <= nums[i] <= limit <= 10^5
n is even.

########################################################################################
Explanation:
Consider nums = [1, 2, 3, 2, 4, 1], limit = 4
Look at this values ---^--^------
You can either swap 3 by a number in (1, 4),
swap 2 by a number in (1, 4),
swap both or none

if we look at the range of the sum:
[2, 3, 4, 5, 6, 7, 8], we have the following necessary moves
[2, 1, 1, 0, 1, 1, 2] in order to achieve each target sum.
We can then calculate the necessary moves for every target sum for each pair,
and choose the target sum with the least amount of moves.

The problem is that this would require looping the target sum array for every pair, which is O(n*limit)
As the target sum vector is composed of intervals, we can calculate only its "derivative" instead.
For the array [2,   1, 1,  0,  1, 1,  2], starting from the left, the derivative is:
              [+2, -1, 0, -1, +1, 0, +1]

If we have the derivative array, we don't need to calculate the whole target sum array,
only its boundaries. Which are:
2 = +2 (change both to 1)
min(n1, n2) + 1 = -1 (change the biggest one to 1)
n1 + n2 = -1 (no change)
n1 + n2 + 1 = +1 (add one to smallest number)
max(n1, n2) + limit + 1 = +1 (we need to change both to achieve targets bigger than this)

Tried to draw a graph of the target sum array and its derivative
 Sum
 2|___               ___
 1|   ______   ______
 0|         ___
 __,__,__,__,__,__,__,__
   2  3  4  5  6  7  8  num

Derivative

 2|  *
 1|  |           *     *
 0|__|__,__*__,__|__*__|_
  |  2  3  4  5  6  7  8
  |     |     |
-1|     *     *
-2|

After we calculated the target sum derivative for every pair,
we add them up and integrate the derivative to obtain the target sum array again
Then we need to return the minimum value in this array.

Complexity:
Time: O(limit) # O(max(N, limit)) but limit >= N
Space: O(limit)
"""
from typing import List


class Solution:
    def min_moves(self, nums: List[int], limit: int) -> int:
        # start the target sum derivative array
        sum_map = [0] * (2 * limit)
        # loop through the pairs
        for i in range(len(nums) // 2):  # O(n)
            # n1 will be min, n2 will be max
            if nums[i] <= nums[-i - 1]:
                n1 = nums[i]
                n2 = nums[-i - 1]
            else:
                n1 = nums[-i - 1]
                n2 = nums[i]
            # calculate the interval boundaries and add to the derivative array
            sum_map[0] += 2
            sum_map[n1 - 1] -= 1
            sum_map[n1 + n2 - 2] -= 1
            sum_map[n1 + n2 - 1] += 1
            sum_map[n2 + limit - 1] += 1

        ret, current_sum = len(nums), 0
        # integrate the derivative array while checking for the minimum value
        for s in sum_map:  # O(limit)
            current_sum += s
            ret = min(ret, current_sum)
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.min_moves([1, 2, 4, 3], 4) == 1
    assert solution.min_moves([1, 2, 2, 1], 2) == 2
    assert solution.min_moves([1, 2, 1, 2], 2) == 0
