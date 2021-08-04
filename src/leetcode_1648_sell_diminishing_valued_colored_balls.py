# @l2g 1648 python3
# [1648] Sell Diminishing-Valued Colored Balls
# Difficulty: Medium
# https://leetcode.com/problems/sell-diminishing-valued-colored-balls
#
# You have an inventory of different colored balls,
# and there is a customer that wants orders balls of any color.
# The customer weirdly values the colored balls.
# Each colored ball's value is the number of balls of that color you currently have in your inventory.
# For example,if you own 6 yellow balls,the customer would pay 6 for the first yellow ball.
# After the transaction,there are only 5 yellow balls left,
# so the next yellow ball is then valued at 5 (i.e.,
# the value of the balls decreases as you sell more to the customer).
# You are given an integer array,inventory,
# where inventory[i] represents the number of balls of the ith color that you initially own.
# You are also given an integer orders,
# which represents the total number of balls that the customer wants.
# You can sell the balls in any order.
# Return the maximum total value that you can attain after selling orders colored balls.
# As the answer may be too large,return it modulo 109 + 7.
#
# Example 1:
#
#
# Input: inventory = [2,5], orders = 4
# Output: 14
# Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
# The maximum total value is 2 + 5 + 4 + 3 = 14.
#
# Example 2:
#
# Input: inventory = [3,5], orders = 6
# Output: 19
# Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
# The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
#
# Example 3:
#
# Input: inventory = [2,8,4,10,6], orders = 20
# Output: 110
#
# Example 4:
#
# Input: inventory = [1000000000], orders = 1000000000
# Output: 21
# Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000.
# 500000000500000000 modulo 109 + 7 = 21.
#
#
# Constraints:
#
# 1 <= inventory.length <= 10^5
# 1 <= inventory[i] <= 10^9
# 1 <= orders <= min(sum(inventory[i]), 10^9)
#
#

from typing import List

"""
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:


Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110
Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 10^9 + 7 = 21.

Constraints:

1 <= inventory.length <= 10^5
1 <= inventory[i] <= 10^9
1 <= orders <= min(sum(inventory[i]), 10^9)
"""


class Solution:
    def calc_partial_sum(self, n, cnt):
        return (
            (n + n - cnt + 1) * cnt
        ) >> 1  # the division / outputs a float which have limited precision. >> ensures that the output is an int

    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # order in descending order
        inventory = sorted(inventory, reverse=True)
        # add a 0 at the end to avoid out of range
        inventory.append(0)
        ret = 0
        mod = 1000000007
        idx = 1
        while orders > 0:
            # get the diference between the current value and the next one
            dif = (
                inventory[idx - 1] - inventory[idx]
            )  # if there is no 0 at the end it crashes here
            # continue until the difference is not zero
            if not dif:
                idx += 1
                continue
            # if dif * the current amount of concurrent balls is bigger than the remaining order
            if dif * idx > orders:
                # we first calculate how many concurrent balls we can calculate together
                max_together = orders // idx
                # concurrent balls + remaing orders times the highest valued balls
                tmp = self.calc_partial_sum(inventory[idx - 1], max_together) * idx + (
                    orders % idx
                ) * (inventory[idx - 1] - max_together)
                ret = ret + tmp
                break
            else:
                tmp = self.calc_partial_sum(inventory[idx - 1], dif) * idx
                ret = ret + tmp
            # update the value of the highest valued balls
            inventory[:idx] = [inventory[idx]] * idx
            orders -= dif * idx
            idx += 1
        return ret % mod


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1648.py")])
