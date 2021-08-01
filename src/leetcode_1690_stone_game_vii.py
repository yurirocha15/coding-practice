# @l2g 1690 python3
# [1690] Stone Game VII
# Difficulty: Medium
# https://leetcode.com/problems/stone-game-vii
#
# Alice and Bob take turns playing a game, with Alice starting first.
# There are n stones arranged in a row.On each player's turn,
# they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row.
# The winner is the one with the higher score when there are no stones left to remove.
# Bob found that he will always lose this game (poor Bob,he always loses),
# so he decided to minimize the score's difference.
# Alice's goal is to maximize the difference in the score.
# Given an array of integers stones where stones[i] represents the value of the ith stone from the left,
# return the difference in Alice and Bob's score if they both play optimally.
#
# Example 1:
#
# Input: stones = [5,3,1,4,2]
# Output: 6
# Explanation:
# - Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
# - Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
# - Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
# - Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
# - Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
# The score difference is 18 - 12 = 6.
#
# Example 2:
#
# Input: stones = [7,90,5,1,100,10,10,2]
# Output: 122
#
# Constraints:
#
# n == stones.length
# 2 <= n <= 1000
# 1 <= stones[i] <= 1000
#
#

import functools
from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pre_sum = [0] + list(accumulate(stones))

        @functools.lru_cache(None)
        def dp(l: int, r: int) -> int:
            if l == r:
                return 0
            return max(
                (pre_sum[r + 1] - pre_sum[l + 1]) - dp(l + 1, r),
                (pre_sum[r] - pre_sum[l] - dp(l, r - 1)),
            )

        ret = dp(0, len(stones) - 1)
        dp.cache_clear()
        return ret


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1690.py")])
