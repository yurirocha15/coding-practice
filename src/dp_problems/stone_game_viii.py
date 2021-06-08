#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1872. Stone Game VIII
URL: https://leetcode.com/problems/stone-game-viii/description/
"""
from functools import reduce
from itertools import accumulate
from typing import List


class Solution:
    def stone_game_v_i_i_i(self, stones: List[int]) -> int:
        return reduce(
            lambda value, pre_sum: max(value, pre_sum - value),
            list(accumulate(stones))[:0:-1],
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.stone_game_v_i_i_i(stones=[-1, 2, -3, 4, -5]) == 5
    assert solution.stone_game_v_i_i_i(stones=[7, -6, 5, 10, 5, -2, -6]) == 13
    assert solution.stone_game_v_i_i_i(stones=[-10, -12]) == -22
