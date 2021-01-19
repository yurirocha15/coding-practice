#!/usr/bin/env python
"""
Platform: LeetCode
1690. Stone Game VII
URL: https://leetcode.com/problems/stone-game-vii/

Description:
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn,
they can remove either the leftmost stone or the rightmost stone
from the row and receive points equal to the sum of the remaining stones' values in the row.
The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses),
so he decided to minimize the score's difference.
Alice's goal is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents
the value of the ith stone from the left,
return the difference in Alice and Bob's score if they both play optimally.


Example 1:
Input: stones = [5,3,1,4,2]
Output: 6
Explanation:
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.

Example 2:
Input: stones = [7,90,5,1,100,10,10,2]
Output: 122

Constraints:
n == stones.length
2 <= n <= 1000
1 <= stones[i] <= 1000
"""
from functools import lru_cache
from itertools import accumulate
from typing import List


class Solution:
    def stone_game_VII(self, stones: List[int]) -> int:
        pre_sum = [0] + list(accumulate(stones))

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left == right:
                return 0
            return max(
                (pre_sum[right + 1] - pre_sum[left + 1]) - dp(left + 1, right),
                (pre_sum[right] - pre_sum[left] - dp(left, right - 1)),
            )

        ret = dp(0, len(stones) - 1)
        dp.cache_clear()
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.stone_game_VII([5, 3, 1, 4, 2]) == 6
    assert solution.stone_game_VII([7, 90, 5, 1, 100, 10, 10, 2]) == 122
